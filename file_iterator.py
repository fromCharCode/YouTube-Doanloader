class FileIterator:
    # class is prototype. maybe will be changed into real iterator, if necessary
    # there is much to do here!

    path = ""

    def __init__(self, path):
        self.path = path

    def get_list_size(self):
        with self.path as file:
            s = 0
            for line in file:
                s += 1
            return s

    # nochmal belesen
    def link_generator(self, path):
        with open(path, "r") as file:
            for line in file:
                yield line
