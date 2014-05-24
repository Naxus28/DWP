class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="css/styles.css">
    </head>
    <body>
        '''
        self._content = "This is my content"
        self.page_content = ""
        self.new_page_content = "<div id='new_pictures'></div>"
        self._close = '''
    </body>
</html>
        '''
        self._css_url = ""
        self._title = ""
        # self.all = self._open + self._content + self._close

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
        self.all = self._open + self._content + self.new_page_content + self._close
        self.all = self.all.format(**locals())




class FormPage(Page):
    def __init__(self):
        #call constructor function
        Page.__init__(self)
        self.__form_open = '<form method=GET action="">'
        self.__inputs = '''
        <input id = "textfield" type = 'text' name='query' placeholder='Search Term'>
        <input id = "button" type = 'submit'>
        '''
        self.__form_close = '</form>'
        self.form_header = "<h1>FUN PICS APP</h1>"
        self._content = self.form_header + self.__form_open + self.__inputs + self.__form_close
        self.all = ""

    def update(self):
        self.all = self._open + self.form_header + self.__form_open + self.__inputs + self.__form_close + \
            self.page_content + self.new_page_content + self._close
        self.all = self.all.format(**locals())

        # print self._content

