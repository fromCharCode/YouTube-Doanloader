import re
import validators

# todo: this must be observable
class YdlModel():

    def __init__(self):
        # those can have an init value.
        self.__format = "mp3"
        self.__outputPath = "./"

        self.__url = ""
        self.__title = ""
        self.__duration = ""
        self.__desc = ""

    def __url_is_valid(self, url):
        # todo: implement regular expression for pattern recognition
        """
        pattern = re.compile(r'^https://www.youtube.com/watch\?v=')
        # test later

        if len(pattern) == 0:
            return False

        """
        return validators.url(url)

    def set_url(self, url):
        if (self.__url_is_valid(url)):
            self.__url = url
        else:
            # todo: url = "" -> reset Hint to exceptional string
            pass

    def set_format(self, fmt):
        self.__format = fmt

    def set_output_path(self, path):
        self.__outputPath = path

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