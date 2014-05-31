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
        self.api_array = []

    def update(self):
        i = 0
        for item in self.api_array:
            self.api_content += '''
                <a href ="?num='''+str(i)+'''">'''+item.title+'''</a>
                '''
            i += 1

            if item[i].
            self.api_content = self.api_content.format(**locals())

