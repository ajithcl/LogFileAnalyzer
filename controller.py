# Date   : 28 May 2022
# Author : Ajith kumar CL
# Notes  : Starting program for this web project.

import web
import json
from models.LogFile import LogFile

web.config.debug = False

urls = ('/', 'Home',
        '/analyze_log_file', 'AnalyzeLogFile')

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"))
# session_data = session.initializer
render = web.template.render("views/templates", base="MainLayout")


class Home:
    def GET(self):
        page_data = {}  # Add any information needs to pass to the page
        return render.Home(page_data)


class AnalyzeLogFile:
    def POST(self):
        json_result = {}
        input_data = web.input()
        try:
            input_logfilename = input_data['log_file_name']
        except NameError:
            json_result['result'] = 'error'
            json_result['data'] = 'Invalid logfile name'
            json_result = json.dumps(json_result)
            return json_result

        logfile_class = LogFile()

        try:
            logfile_class.logfile_name = input_logfilename
        except FileNotFoundError:
            json_result['result'] = 'error'
            json_result['data'] = 'Log File not found'
            json_result = json.dumps(json_result)
            return json_result

        processing_result = logfile_class.process_logfile()

        json_result = {'result': 'success',
                       'data': processing_result}
        json_result = json.dumps(json_result)

        return json_result


"""
Run the application
"""
if __name__ == "__main__":
    app.run()
