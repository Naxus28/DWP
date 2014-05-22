class Page(object):
    def __init__(self):
        self.__title = "Home Page"
        self.__open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>

    </head>
    <body>
        '''
        self._button = "<a href='?name=the_function'" + "{self.number}>""CLICK</a>"
        self._number_one = "<p>{self.number}</p>"
        self.__close = '''
    </body>
</html>
        '''
        self._count = 0
        self.__all = self.__open + self._button + str(self._count) + self.__close
        self.title = "Change Number"






