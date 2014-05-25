class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="css/styles.css">
        <link href='http://fonts.googleapis.com/css?family=Lustria|Marcellus+SC|Brawler|Fontdiner+Swanky|Handlee|Libre+Baskerville|Architects+Daughter|Forum' rel='stylesheet' type='text/css'>
    </head>
    <body>
        '''
        self.header = "<h1>Picture Mosaic API</h1>"
        self._content = ""
        self._close = '''
    </body>
</html>
        '''
        self.searched_pictures = ""
        self.page_content = ""
        self._css_url = ""
        self._title = ""
        self.all = self._open + self.header + self._content + self._close

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self, c):
            self._css_url = c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())

    # def print_out_new_pics(self):
    #     return self.searched_pictures




class FormPage(Page):
    def __init__(self):
        #call constructor function
        Page.__init__(self)

        self.__form_open = '<form method=GET action="">'
        self.__inputs = '''
        <input id = "textfield" type = 'text' name='query' placeholder='Search Term'>
        <input id = "button" type = 'submit' value="SEARCH">
        '''
        self.__form_close = '</form>'
        self._content = self.__form_open + self.__inputs + self.__form_close
        self.all = ""


    def update(self):
        self.all = self._open + self.header + self.__form_open + self.__inputs + self.__form_close + \
            self.page_content + self.searched_pictures + self._close
        self.all = self.all.format(**locals())




