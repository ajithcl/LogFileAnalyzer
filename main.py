# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ConfigurationSettings import ConfigurationSettings
from FilterFile import FilterFileLoader


def print_hi():
    cs = ConfigurationSettings()

    filter_file_name = cs.filter_file
    print (f"Filter file from configuration file : {filter_file_name}")
    try:
        filter_file = FilterFileLoader(filterfilename=filter_file_name)
    except FileNotFoundError as notfoundferror :
        print (f"Error loading filter file {notfoundferror.strerror}")
        return
    except NameError as ne:
        print (ne.__str__())
        return
    filter_file_contents = filter_file.get_filter_file()
    print (filter_file_contents)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
