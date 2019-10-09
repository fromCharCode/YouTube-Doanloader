from ydl_controller_interface import YdlControllerInterface
from ydl_model import YdlModel
from ydl_view import YdlView
from action_listener_interface import ActionListenerInterface


class YdlController(YdlControllerInterface):

    def __init__(self, model: YdlModel):
        self.__model = model
        self.__views = []

    def add_view(self, view: YdlView):
        self.__views.append(view)

    def action_performed(self, e: ActionListenerInterface):
        pass
