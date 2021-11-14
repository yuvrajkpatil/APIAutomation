# -*- coding: utf-8 -*-
import config
import time

# This payload is used for registering user without language field
USER_VALID = {
    'name': 'Test User %s' % time.time(),
    'email': 'test.user.%s' % (str(time.time()) + config.DOMAIN),
    'password': 'Qwerty@123'
}

# This payload is used for registering user with language field
USER_WITH_LANG = {
    'name': 'Test User %s' % time.time(),
    'email': 'test.user.%s' % (str(time.time()) + config.DOMAIN),
    'password': 'Qwerty@123',
    'language': 'de'
}

# This payload is used for verifying register user error when name field is not provided in payload
USER_NAME_MISSING = {
    'email': 'test.user.%s' % (str(time.time()) + config.DOMAIN),
    'password': 'Qwerty@123'
}

# This payload is used for verifying register user error when email field is not provided in payload
USER_EMAIL_MISSING = {
    'name': 'Test User %s' % time.time(),
    'password': 'Qwerty@123'
}

# This payload is used for verifying register user error when password field is not provided in payload
USER_PASSWORD_MISSING = {
    'name': 'Test User %s' % time.time(),
    'email': 'test.user.%s' % (str(time.time()) + config.DOMAIN),
}

# This payload is used for verifying register user error when invalid name(only 2 characters in namae) is provided in payload
USER_INVALID_NAME = {
    'name': 'ab',
    'email': 'test.user.%s' % (str(time.time()) + config.DOMAIN),
    'password': 'Qwerty@123'
}

# This payload is used for verifying register user error when invalid email(@ character is missing) is provided in payload
USER_INVALID_EMAIL = {
    'name': 'Test User %s' % time.time(),
    'email': 'test.user.' + config.DOMAIN[1:],
    'password': 'Qwerty@123'
}

# This payload is used for verifying register user error when invalid password(less than 8 characters) is provided in payload
USER_INVALID_PASSWORD = {
    'name': 'Test User %s' % time.time(),
    'email': 'test.user.%s' % (str(time.time()) + config.DOMAIN),
    'password': 'Qwerty@'
}
