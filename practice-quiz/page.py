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
        self._number_one = "<p>{self.number}</p>"
        self._button = "<a href='?name=the_function'>Count Up</a>"
        self.__close = '''
    </body>
</html>
        '''
        self._count = 0
        self.__all = self.__open + self._number_one + self._button + self.__close
        self.title = "Change Number App"

    @property
    def number(self):
        return self._count

    @number.setter
    def number(self, new_number):
        self._count = self._count + new_number

    def print_out(self):
        self.update()
        return self.__all

    def update(self):
        #replaces all the {} with the values of the corresponding variables
        self.__all = self.__all.format(**locals())




