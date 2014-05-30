from model import ApiDataObject

class PageView(object):
    def __init__(self):
        self.open = '''
        <!DOCTYPE html>
        <html lang='en'>
            <head>
                <title>Exam Practice</title>
            </head>
            <body>'''
        self.content = "page content"
        self.close = '''
            </body>
        </html>
                '''

        self.all = ""

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.open + self.content + self.close


class ApiView(object):
    def __init__(self):
        self.view_data = ApiDataObject()
        #print self.view_data
        self.api_content = ""

    def update(self):
        self.api_content = '''
                <h1>Weather App Test</h1>
                <p>Country: {self.view_data.country}</p>
                <p>Condition: {self.view_data.weather}</p>
                <p>Description: {self.view_data.description}</p>
                <p> Temperature: {self.view_data.temp}</p>
        '''
        self.api_content = self.api_content.format(**locals())

        #print self.api_content