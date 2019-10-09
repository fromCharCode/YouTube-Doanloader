import ydl_controller_interface
import ydl_model
from observer import Observer


class YdlView(Observer):

    def __init__(self, model: ydl_model.YdlModel, controller: ydl_controller_interface):
        self.__model = model
        self.__controller = controller
        model.subscribe(self) # todo: research if this one goes into controller

        self.__title = ""
        self.__duration = ""
        self.__url = ""

    def get_controller(self):
        return self.__controller

    def show_validation(self):
        pass

    def show_title(self):
        pass

    def show_duration(self):
        pass

    def update(self):
        # This is meant to be an INTERFACE (python do not need them as java does)
        # todo: implement update logics here!!!
        self.__title = self.__model.get_title()
        self.__duration = self.__model.get_duration()
        self.__url = self.__model.get_url()
