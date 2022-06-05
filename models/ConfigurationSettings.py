"""
Takes care of the Configurations settings
from the configuration ini file
"""
from configparser import ConfigParser


class ConfigurationSettings:
    def __init__(self):
        self._filter_file = ''
        self.config_parser = ConfigParser()
        try:
            self.config_parser.read('config.ini')
            self._filter_file = self.config_parser.get("FilterFile", "FileName")
        except FileExistsError as file_error:
            return f"Invalid Configuration {file_error.strerror}"

    @property
    def filter_file(self):
        return self._filter_file

    def get_search_key_words(self):
        return self.config_parser.get(section='SearchKeyWords', option='words')
