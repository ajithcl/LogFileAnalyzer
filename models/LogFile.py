import json

from models.ConfigurationSettings import ConfigurationSettings
from models.FilterFile import FilterFileLoader
from os.path import exists


class LogFile:
    def __init__(self):
        self._output_file_list = []
        self.filter_contents_list = []
        self._logfile_name = ''
        self.logfile_lines_total = 0

    @property
    def logfile_name(self):
        return self._logfile_name

    @logfile_name.setter
    def logfile_name(self, input_logfilename):
        if exists(input_logfilename):
            self._logfile_name = input_logfilename
        else:
            raise FileNotFoundError

    def process_logfile(self):
        cs = ConfigurationSettings()
        filter_file_name = cs.filter_file

        try:
            filter_file = FilterFileLoader(filterfilename=filter_file_name)
        except FileNotFoundError as notfounderror:
            print("file not found")  # ToDO
            return
        except NameError as name_error:
            print(name_error.__str__())  # ToDO
            return

        self.filter_contents_list = filter_file.get_filter_file()

        with open(self._logfile_name) as file_logfile:
            for line_content in file_logfile:
                self.process_lines(line_content=line_content)

        output_file_name = self.export_to_file()

        result = {'log_file_line_count': self.logfile_lines_total,
                  'output_file_line_count': len(self._output_file_list),
                  'output_file_name' : output_file_name}
        json_result = json.dumps(result)

        return json_result

    def process_lines(self, line_content):
        should_exclude = False
        self.logfile_lines_total += 1

        for filter in self.filter_contents_list:
            if line_content.__contains__(filter):
                should_exclude = True
                break
        if not should_exclude:
            self._output_file_list.append(line_content)

    def export_to_file(self):
        output_file_name = 'D:\\Ajith\\PythonProject\\LogFileAnalyzer\\output.txt'
        with open(output_file_name, 'w') as output_file:
            for line in self._output_file_list:
                output_file.write(line)
        return output_file_name
