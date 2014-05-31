from model import ApiDataObject

class PageView(object):
    def __init__(self):
        self.__open = '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>DPW Final Exam | Top 10 Songs</title>
            </head>
            <body>
        '''
        self.content = "<p>the content</p>"

        self.__close = '''
            </body>
        </html>
        '''
        self._all = self.__open + self.content + self.__close

    def print_out(self):
        self.update()
        return self._all

    def update(self):
        self._all = self.__open + self.content + self.__close


class ApiView(object):
    def __init__(self):
        self.data_view = ApiDataObject()
        self.api_content = ""

    def update(self):
        # for item in self.data_view.all_items:
            self.api_content = '''
                <a href ="?{self.data_view.artist}">The Artist</a>
                '''

            # self.api_content = self.api_content.format(**locals())

           # print self.api_content