# -*- coding: utf-8 -*-
from dataclasses import dataclass
import requests


@dataclass
class Response:
    """This class is used to send api response with required attributes"""
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:
    """
    This class implements methods which actually does requests modules method calls
    """
    def get(self, url):
        """This method does GET requests call for given url and returns received response as Response class object"""
        response = requests.get(url)
        return self.__get_responses(response)

    def post(self, url, payload, headers):
        """This method does POST requests call for given url with given payload and headers.
        Returns received response as Response class object"""
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, url, headers):
        """This method does DELETE requests call for given url with headers.
        Returns received response as Response class object"""
        response = requests.delete(url, headers=headers)
        return self.__get_responses(response)

    def __get_responses(self, response):
        """This method converts the received response as a Response objects and returns it"""
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
        except Exception as fault:
            logger.info('Error occurred during response conversion to json. Error: %s', str(fault))
            logger.exception(fault)
            as_dict = {}
        headers = response.headers
        return Response(status_code, text, as_dict, headers)
