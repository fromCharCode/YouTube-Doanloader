# import something for getting error codes
import validators
import re

def check(link):

    # todo: check if is not working link, but yet valid

    # regular expression - must be with this beginning:
    pattern = re.compile(r'^https://www.youtube.com/watch\?v=') # .youtube.com/watch?v=[a-z0-9]{11,}

    #print(re.search(r'https://www\.youtube\.com/watch?v=\W{11,}', link))

    matches = pattern.finditer(link)

    for match in matches:
        print(match)

    return validators.url(link)


    # https://www.youtube.com/watch?v=ehs6vQTFPoA
    # return validation
    #return validators.url(link)

