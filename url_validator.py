# import something for getting error codes
import validators

def check(link):

    # must be a YouTube link
    if ("www.youtube." not in link):
        return False

    # must not be a standard page
    if ((link == "https://www.youtube.com/" ) or (link == "https://www.youtube.de/")):
        return False

    # todo: check if is not working link, but yet valid

    # return validation
    return validators.url(link)

