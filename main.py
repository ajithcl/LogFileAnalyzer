# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ConfigurationSettings import ConfigurationSettings


def print_hi():
    cs = ConfigurationSettings()

    filter_file_name = cs.filter_file
    print (f"Filter file from configuration file : {filter_file_name}")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
