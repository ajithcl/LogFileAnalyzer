# Date   : 28 May 2022
# Author : Ajith kumar CL
# Notes  : Starting program for this web project.

import requests
import web

web.config.debug = False

urls = ('/', 'Home',
        '/analyze_log_file', 'AnalyzeLogFile')

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"))
session_data = session.initializer
render = web.template.render("views/templates", base="MainLayout")


class Home:
    def GET(self):
        page_data = {}  # Add any information needs to pass to the page
        return render.Home(page_data)

class AnalyzeLogFile:
    def POST(self):
        form_data = web.input()
        print ('Hare Krishna', form_data)

"""
Run the application
"""
if __name__ == "__main__":
    app.run()
