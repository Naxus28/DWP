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
        self.header = "<h1>The Picture Mosaic</h1>"
        self._content = ""
        self._close = '''
        <script src="js/jquery-1.11.0.min.js"></script>
        <script src="js/init.js"></script>
    </body>
</html>
        '''
        self.open_pictures_container = ""
        self.close_pictures_container = ""
        self.searched_pictures = ""
        self.page_content = ""
        self._title = "The Picture Mosaic | Powered by Flickr"
        self.all = self._open + self.header + self._content + self._close

    @property
    def title(self):
        return self._title

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
        self.all = self._open + self._content + self.open_pictures_container + self.close_pictures_container + self._close
        self.all = self.all.format(**locals())

    # def print_out_new_pics(self):
    #     return self.searched_pictures




class FormPage(Page):
    def __init__(self):
        #call constructor function
        Page.__init__(self)

        self.__form_open = '<form method=GET action="">'
        self.__inputs = '''
        <input id = "textfield" type = 'text' name='query' placeholder='Search Picture'>
        <input id = "button" type = 'submit' value="SEARCH">
        '''
        self.__form_close = '</form>'
        self.open_pictures_container = "<div id = 'results_wrapper'>"
        self.close_pictures_container = "</div>"

        self._content = self.__form_open + self.__inputs + self.__form_close
        self.all = ""
        self.search_results_header = ""
        self._arrow = "<img id = 'arrow' src = 'images/arrow1.png'/>"

    def update(self):
        self.all = self._open + self.header + self.__form_open + self.__inputs + self.__form_close + \
            self.page_content + self.open_pictures_container + self.search_results_header + self.searched_pictures + \
            self._arrow + self.close_pictures_container + self._close
        self.all = self.all.format(**locals())

    @property
    def search_header_update(self):
        return self.search_results_header

    @search_header_update.setter
    def search_header_update(self, new_header):
        self.search_results_header = new_header