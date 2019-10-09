from observable import Observable

"""
This class must be implemented when the sub class
shall be informed when a value changed
"""


class Observer:

    def __init__(self):
        print("Observer initialized")

    # call change
    def update(self):
        pass
