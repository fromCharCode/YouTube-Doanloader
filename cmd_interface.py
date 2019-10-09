# todo: this file may not be deprecated yet. it could later be a child of the view

import os
import colorama


# class CMDInterface(YdlView)
class CmdInterface():

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
