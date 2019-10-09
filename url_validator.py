"""
This entire file is deprecated and will be deleted when MVC is working
"""


# import something for getting error codes
import validators
import re
import logging

logger = logging.getLogger(__name__)  # now we use logger.debug, etc.
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(style="{", fmt="{asctime} [{levelname}] {message}", datefmt="%d.%m.%Y %H:%M:%S")

file_handler = logging.FileHandler('url_validator.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def url_is_valid(link):

    '''
    # regular expression - must be with this beginning:
    pattern = re.compile(r'^https://www.youtube.com/watch\?v=')
    # test later
    if len(pattern)== 0:
        return False
    '''
    return validators.url(link)


    # link for testing purposes: https://www.youtube.com/watch?v=ehs6vQTFPoA

