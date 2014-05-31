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
        self.api_content = "<p>api content</p>"
        self.__close = '''
            </body>
        </html>
        '''
        self._all = self.__open + self.content + self.api_content + self.__close

    def print_out(self):
        self.update()
        return self._all

    def update(self):
        self._all = self.__open + self.content + self.api_content + self.__close


class ApiView(object):
    def __init__(self):
        self.data_view = ApiDataObject()
        self.api_content = ""
        self.api_new_content = ""
        self.api_array = []


    def update(self):
        i = 0
        for item in self.api_array:
            #print self.api_array[0].title
            self.api_content += '''
                <a style="display:block" href="?num='''+str(i)+'''">'''+item.title+'''</a></br>
                '''
            self.api_new_content = '''
            <p>File: <audio controls><source src=" '''+self.api_array[i].file+''' " type="audio/mp3"></audio></p>
            <p>Title: '''+self.api_array[i].title+'''</p>
            <p>Artist: '''+self.api_array[i].artist+'''</p>
            <p>Length: '''+self.api_array[i].length+'''</p>
            <p>Year: '''+self.api_array[i].year+'''</p>
            <p>Label: '''+self.api_array[i].label+'''</p>
            <p>Cover: <br><img src =" '''+self.api_array[i].cover+''' "/></p>

            '''
            i += 1




