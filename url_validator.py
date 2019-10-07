# import something for getting error codes
import validators
import re

def url_is_valid(link):

    # todo: check if is not working link, but yet valid

    # regular expression - must be with this beginning:
    pattern = re.compile(r'^https://www.youtube.com/watch\?v=') # .youtube.com/watch?v=[a-z0-9]{11,}

    # todo: print matches in debugger (log.debug)

    return validators.url(link)


    # https://www.youtube.com/watch?v=ehs6vQTFPoA
    # return validation
    #return validators.url(link)

