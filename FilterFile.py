import os


class FilterFileLoader:
    def __init__(self, filterfilename=None):
        if not  os.path.exists(filterfilename):
            raise FileNotFoundError
        if os.stat(filterfilename).st_size == 0:
            raise NameError("File empty")
        self.filter_file_name = filterfilename

    def get_filter_file(self):
        with open (self.filter_file_name, 'r') as filter_file:
            data = filter_file.read()
        return data

