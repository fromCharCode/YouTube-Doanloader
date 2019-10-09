from ydl_view import YdlView
from ydl_model import YdlModel
from action_listener_interface import ActionListenerInterface

# need to inherit from an action event listener
class YdlControllerInterface():

    def __init__(self):
        self.__views =[]

    # todo: !!! important: e must be ActionEvent. Not implemented yet
    def action_performed(self, e: ActionListenerInterface):
        pass

    def add_view(self, view: YdlView):
        self.__views.append(view)
