from observer import Observer


"""
This is the subject, the base class of each sub class
that shall offer an subscribe/ publish mechanism
"""


class Observable:

    # print for us! remove later. init observer list
    def __init__(self):
        print("Observable initialized")
        self.__registered_observers = []

    # register an observer if not registered yet
    def subscribe(self, observer: Observer):
        if observer not in self.__registered_observers:
            self.__registered_observers.append(observer)

    # remove observer
    def unsubscribe(self, observer: Observer):
        if observer in self.__registered_observers:
            self.__registered_observers.remove(observer)
        else:
            # log later
            print("Observer: ", observer, " is not registered")

    # go through all observers and call their update()
    def notify_observers(self):
        for observer in self.__registered_observers:
            observer.update()
