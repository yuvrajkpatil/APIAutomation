# -*- coding: utf-8 -*-
from json import dumps
import config
import time
from utils.request import APIRequest
import random
import string


class UserClient:
    """This class will implement all API calls for user object"""
    def __init__(self):
        self.request = APIRequest()
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def get_password(self, length=8):
        """This method is used to get random 8(default) characters password string."""
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def __get_register_user_payload(self, language=''):
        """
        This method is used to get payload for register user api call
        :param language: (str) language code which needs to be added in payload
        :return: payload as dictionary for registering user
        """
        timestamp = int(time.time())
        payload = {
            'name': 'Test User %s' % timestamp,
            'email': 'test.user.%s' % (str(timestamp) + config.DOMAIN),
            'password': self.get_password()
        }
        # Add language to payload if language argument is provided
        if language:
            payload['language'] = language
        return payload

    def register_user(self, payload=None, language=''):
        """
        This method calls register user method of APIRequest class from utils.request file and returns received response
        :param payload: (dict) Payload for user registration
        :param language: (str) IDO 639-1 or 639-2 language code
        :return: Register user api response received from APIRequest.post method
        """
        if payload is None:
            payload = self.__get_register_user_payload(language=language)

        response = self.request.post(config.API_ENDPOINTS['register_user'], dumps(payload), self.headers)
        return payload, response

    def delete_user(self, password, token):
        """
        This method calls delete user method of APIRequest class from utils.request file and returns received response
        :param password: (str) Password of user which needs to be deleted
        :param token: (str) JWT Token for authorization to delete user
        :return: Delete user api response received from APIRequest.delete method
        """
        url = config.API_ENDPOINTS['delete_user'] + '?password=%s' % password
        logger.info('Delete User API URL: %s', url)
        headers = self.headers
        headers['Authorization'] = 'Bearer %s' % token
        logger.info('Delete API Request Headers: %s', headers)
        response = self.request.delete(url, headers)
        return response
