# -*- coding: utf-8 -*-

import requests
BASE_URI = 'https://api.opensensemap.org'
DOMAIN = '@a.com'
API_ENDPOINTS = {
            'register_user': BASE_URI + '/users/register',
            'delete_user': BASE_URI + '/users/me'
        }

EXP_RESPONSES = {
    'success': {
        'status_code': requests.codes.created,
        "code": "Created",
        "message": "Successfully registered new user"
    },
    'duplicate_entry': {
        'status_code': requests.codes.unprocessable_entity,
        "code": "BadRequest",
        "message": "Duplicate user detected"
    },
    'missing_name': {
        'status_code': requests.codes.bad_request,
        "code": "BadRequest",
        "message": "missing required parameter name"
    },
    'invalid_name': {
        'status_code': requests.codes.unprocessable_entity,
        "code": "UnprocessableEntity",
        "message": "Validation failed: Parameter name must consist of at least 3 and up to 40 alphanumerics (a-zA-Z0-9), dot (.), dash (-), underscore (_) and spaces."
    },
    'missing_email': {
        'status_code': requests.codes.bad_request,
        "code": "BadRequest",
        "message": "missing required parameter email"
    },
    'invalid_email': {
        'status_code': requests.codes.unprocessable_entity,
        "code": "UnprocessableEntity",
        "message": "Parameter email is not parseable as datatype email"
    },
    'missing_password': {
        'status_code': requests.codes.bad_request,
        "code": "BadRequest",
        "message": "missing required parameter password"
    },
    'invalid_password': {
        'status_code': requests.codes.unprocessable_entity,
        "code": "UnprocessableEntity",
        "message": "Validation failed: must be at least 8 characters."
    },
    'invalid_language': {
        'status_code': requests.codes.unprocessable_entity,
        "code": "UnprocessableEntity",
        "message": "Parameter language is not parseable as datatype String"
    },
    'delete_success': {
        'status_code': requests.codes.ok,
        "code": "Ok",
        "message": "User and all boxes of user marked for deletion. Bye Bye!"
    }
}

