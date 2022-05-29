# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from models.ConfigurationSettings import ConfigurationSettings
from models.FilterFile import FilterFileLoader

total_line_count = 0
filter_contents_list = []
output_file_list = []

def main_program():
    global filter_contents_list
    cs = ConfigurationSettings()

    filter_file_name = cs.filter_file
    print (f"Filter file from configuration file : {filter_file_name}")
    try:
        filter_file = FilterFileLoader(filterfilename=filter_file_name)
    except FileNotFoundError as notfoundferror :
        print (f"Error loading filter file {notfoundferror.strerror}")
        return
    except NameError as name_error:
        print (name_error.__str__())
        return

    filter_contents_list = filter_file.get_filter_file()

    # read the actual log file
    log_file_name = "test.txt"    #TODO : Get the log filename
    with open(log_file_name) as log_file:
        for line in log_file:
            process_lines(line)

    output_to_text_file()
    print (f"process completed {total_line_count} \n {len(output_file_list)}")



def process_lines(log_line):
    global total_line_count 
    global filter_contents_list
    should_exclude = False

    total_line_count +=1
    for filter in filter_contents_list:
        if log_line.__contains__(filter):
            should_exclude = True
            break
    if not should_exclude:
        output_file_list.append(log_line)

def output_to_text_file():
    with open("output.txt", "w") as opf:
        for line in output_file_list:
            opf.write(line)

    





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_program()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
