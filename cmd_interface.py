import os
import colorama


class CmdInterface:

    # Todo: therer shall be interfaces for linux, cmd, gui, etc.
    # Todo: create method to save in specific folder. config file is needed, therefore and ydl format
    # Todo: this must be the child of a interface class above, which will be shared by any new interface

    # reminder: in windows 10 Strg+V for console may be right click with mouse

    askClear = False
    clear = lambda: os.system('cls')

    def __init__(self):
        colorama.init()
        self.clear()
        self.welcome()

    def welcome(self):
        print("//////////////////////////////////////////////////////\n"
              "///   Youtube Download-Tool - Version Alpha 0.1   ///")
        # this could be bigger. but this is category D (Eisenhower)

    def get_link(self):
        if not self.askClear:
            self.clear()
        print("Insert link, press 1 for entering a path or press e to exit")
        link = input()
        if "https://www.youtube.com/watch?v=" not in link and link != "e" and link != "1":
            self.fail()
            # look at this crap above. we will need a list of commands each attached to a logical function in run

        return link

    def fail(self):
        print("This seems not to be an valid YouTube link.\n press enter to continue")
        input()
        self.get_link()

    def change_ask_clear(self):
        self.askClear = not self.askClear

    # implement logic here later?
    # brainstorm what can be done, what
    # shall be done in what part
    # this is menu interface
    # a menu should always be build around an existing logic,
    # but with implementing the api
