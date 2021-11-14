# -*- coding: utf-8 -*-
from utils.user_client import UserClient
import pytest
import config
import register_user_test_data as test_data
client = UserClient()


@pytest.fixture()
def verify_api_response():
    def wrapper(payload, response, exp_response_key='success'):
        """
        This fixture is used to verify Register User API Response.

        :param payload: (dict) Payload used to call api. From this dictionary we will get expected user name, email and language
        :param response: (object) Response class object from utils.requests file. Contains status_code, text, as_dict, headers attributes
        :param exp_response_key: (str) Expected response key to get expected response dict for particular test case from config.EXP_RESPONSES dict
        :return None
        """
        logger.info('Expected Response Key: %s', exp_response_key)
        # Get the expected API response details like status_code, code and message
        exp_response = config.EXP_RESPONSES.get(exp_response_key, None)
        logger.info('Expected Response: %s', exp_response)

        # Check if expected response is available in config.EXP_RESPONSES dict for exp_response_key and fail test case if it's not available
        if exp_response is None:
            assert False, 'Please provide correct expected error.'

        assert response.status_code == exp_response[
            'status_code'], 'Actual [%s] & Expected [%s] status code do not match' % (
        response.status_code, exp_response['status_code'])
        assert response.as_dict['code'] == exp_response['code'], 'Actual [%s] & Expected [%s] code do not match' % (
        response.as_dict['code'], exp_response['code'])
        assert response.as_dict['message'] == exp_response[
            'message'], 'Actual [%s] & Expected [%s] message do not match' % (
        response.as_dict['message'], exp_response['message'])

        # Additionally verify token, refresh token and user details for successful API call
        if exp_response_key == 'success':
            assert response.as_dict['token'] is not None, 'JWT token is not received in API Response'
            assert response.as_dict['refreshToken'] is not None, 'Refresh token is not received in API Response'
            assert verify_user_dict(get_expected_user_dict(payload), response.as_dict['data'][
                'user']), 'Expected and Actual user details received in API Response do not match'
    return wrapper


@pytest.fixture()
def cleanup():
    def wrapper(password, jwt):
        """This method does cleanup. Deletes created user. Password and JWT Token are required to call delete user api"""
        logger.info('Password: %s, JWT: %s', password, jwt)
        logger.info('Deleting registered user for successful user creation')
        response = client.delete_user(password, jwt)
        logger.info('Delete User API Response: %s', response)
        exp_response = config.EXP_RESPONSES['delete_success']
        assert response.status_code == exp_response[
            'status_code'], 'Actual [%s] & Expected [%s] status code do not match' % (
            response.status_code, exp_response['status_code'])
    return wrapper


def verify_user_dict(expected, actual):
    """
    This method verifies expected(formed) and actual(in api response) user dictionary.
    :param expected: (dict) Formed expected user dict
    :param actual: (dict) Actual user dict received in successful register user api response
    :return: True if key and values from both dictionary matches. Else False
    """
    logger.info('User Dict.\nExpected: %s\nActual: %s', expected, actual)

    # Get the keys which are extra in API Response or keys for whom values are not matching with expected
    not_matching_fields = {key: actual[key] for key in actual if key not in expected or actual[key] != expected[key]}
    logger.info('Not matching user fields: %s', not_matching_fields)

    # Verify there are no differences between expected and actual user dict
    return not_matching_fields == {}


def get_expected_user_dict(payload):
    """
    This method is used to get expected user dictionary to compare it with successful api response user dictionary
    :param payload: (dict) Payload used to call api. From this dictionary we will get expected user name, email and language
    :return user: (dict) Expected user dict to compare against successful api response received user dict
    """
    user = {
        'name': payload['name'],
        'email': payload['email'],
        'role': 'user',
        'language': payload['language'] if payload.get('language', None) else 'en_US',
        'boxes': [],
        'emailIsConfirmed': False
    }
    return user


def get_payload_for_failure_test_cases(error):
    """
    This method is used to get expected payload for particular error key.

    :param error: Expected error key for which we want to get payload.
    :returns payload from register_user_test_data file for provided error key
    """
    logger.info('Expected Error Key: %s', error)
    if error.lower() == 'missing_name':
        payload = test_data.USER_NAME_MISSING
    elif error.lower() == 'missing_email':
        payload = test_data.USER_EMAIL_MISSING
    elif error.lower() == 'missing_password':
        payload = test_data.USER_PASSWORD_MISSING
    elif error.lower() == 'invalid_name':
        payload = test_data.USER_INVALID_NAME
    elif error.lower() == 'invalid_email':
        payload = test_data.USER_INVALID_EMAIL
    elif error.lower() == 'invalid_password':
        payload = test_data.USER_INVALID_PASSWORD
    else:
        payload = {}
        logger.info('Please provide correct error key.')
    return payload


@pytest.mark.p0
def test_register_user_with_default_language(verify_api_response, cleanup):
    """
    This Test Case verifies user gets registered successfully with valid payload.
    Also verifies by default user language is set as 'en_US' when language is not provided in payload
    """
    try:
        # Call Register User API and get payload provided and actual api response
        payload, response = client.register_user(payload=test_data.USER_VALID)
        logger.info('Register User API. Payload: %s, Response: %s', payload, response)

        # Verify actual and expected api response
        verify_api_response(payload, response)
    except Exception as fault:
        logger.info('Exception occurred in test case. Error: %s', str(fault))
        logger.exception(fault)
    finally:
        # Cleaning up created user in case of successful user creation
        if response.status_code == 201:
            cleanup(payload['password'], response.as_dict['token'])


@pytest.mark.p0
def test_register_user_with_non_default_language(verify_api_response, cleanup):
    """
    This Test Case verifies user gets registered successfully with valid language provided in payload.
    """
    try:
        # Call Register User API and get payload provided and actual api response
        payload, response = client.register_user(payload=test_data.USER_WITH_LANG)
        logger.info('Register User API. Payload: %s, Response: %s', payload, response)

        # Verify actual and expected api response
        verify_api_response(payload, response)
    except Exception as fault:
        logger.info('Exception occurred in test case. Error: %s', str(fault))
        logger.exception(fault)
    finally:
        # Cleaning up created user in case of successful user creation
        if response.status_code == 201:
            cleanup(payload['password'], response.as_dict['token'])


@pytest.mark.p1
@pytest.mark.parametrize('error', ['missing_name', 'missing_email', 'missing_password', 'invalid_name', 'invalid_email',
                                   'invalid_password'])
def test_register_user_failure(error, verify_api_response):
    """
        This Data Driven Test Case verifies below failure scenarios for user registration
        1. missing_name: Name field is not provided in payload.
        2. missing_email: Email field is not provided in payload.
        3. missing_password: Password field is not provided in payload.
        4. invalid_name: Invalid Name field value is provided in payload.
        5. invalid_email: Invalid Email field value is provided in payload.
        6. invalid_password: Invalid Password field value is provided in payload.
    """
    logger.info('Verifying error: %s', error)

    # Get payload for user creation failure scenario
    payload = get_payload_for_failure_test_cases(error)
    logger.info('Payload for Register User API: %s', payload)

    # Call Register User API and get payload provided and actual api response
    payload, response = client.register_user(payload=payload)
    logger.info('Register User API. Payload: %s, Response: %s', payload, response)

    # Verify actual and expected api response for particular error
    verify_api_response(payload, response, error)
