import builtins
import pytest
import os
import logging


@pytest.fixture(autouse=True, scope='session')
def get_logger():
    log_dir = 'logs'
    # Create logs directory if not exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(os.path.join(log_dir, "testlog.log"), mode='w')
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)-8s] %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    builtins.logger = logger


