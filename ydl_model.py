import re
import validators
from observable import Observable


class YdlModel(Observable):

    def __init__(self):
        # those can have an init value.
        self.__format = "mp3"
        self.__outputPath = "./"

        self.__url = ""
        self.__title = ""
        self.__duration = ""
        self.__desc = ""

    # validation
    def __url_is_valid(self, url):
        # todo: implement regular expression for pattern recognition
        # ' https://www.youtube.com/watch?v='
        """
        pattern = re.compile(r'^https://www.youtube.com/watch\?v=')
        # test later

        if len(pattern) == 0:
            return False

        """
        return validators.url(url)

    # setters
    def set_url(self, url):
        if (self.__url_is_valid(url)):
            self.__url = url
        else:
            self.__url = ""
        self.notify_observer()

    def set_format(self, fmt):
        self.__format = fmt
        self.notify_observer()

    def set_output_path(self, path):
        self.__outputPath = path
        self.notify_observer()

    # getters
    def get_format(self):
        return self.__format

    def get_output_path(self):
        return self.__outputPath

    def get_title(self):
        return self.__title

    def get_duration(self):
        return self.__duration

    def get_desc(self):
        return self.__desc

    def get_url(self):
        return  self.__url
