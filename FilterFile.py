from os.path import exists


class FilterFileLoader:
    def __init__(self, filterfilename=None):
        if not exists(filterfilename):
            return FileNotFoundError
        self.filter_file_name = filterfilename

    def load_file(self):
        pass
