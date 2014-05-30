from model import ApiDataObject

class PageView(object):
    def __init__(self):
        self.page_open = '''
        <!DOCTYPE html>
        <html lang='en'>
            <head>
            </head>
            <body>
        '''
        self.page_content = "Content"
        self.page_close = '''
            </body>
        </html>
        '''

        self.all = self.page_open + self.page_content + self.page_close

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.page_open + self.page_content + self.page_close


class ApiView(object):
    def __init__(self):
        self.data_view = ApiDataObject()
        self.api_content = ""

    def update(self):
        self.api_content = '''
        <p>Temperature: {self.data_view.temp}</p>
        <p>Min Temperature: {self.data_view.temp_min}</p>
        <p>Max Temperature : {self.data_view.temp_max}</p>
        <p>Humidity: {self.data_view.humidity}</p>
        <p>Wind Speed: {self.data_view.wind_speed}</p>
'''
        self.api_content = self.api_content.format(**locals())

        print self.api_content