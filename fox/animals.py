class Animals(object):
    def __init__(self):

        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href={self.css_url}>
    </head>
    <header>
        <h1>The Animals Page</h1>
    </header>
    <body>
        '''
        self._content = '''
        <div id="info">
            <h2>This is the {self.animal}</h2>
            <p>{self._phylum}</p>
            <p>{self._class_}</p>
            <p>{self._order}</p>
            <p>{self._family}</p>
            <p>{self._genus}</p>
            <p>{self._avg_lifespan}</p>
            <p>{self._habitat}</p>
            <p>{self._geo_location}</p>
            <p>{self._url}</p>
        </div>
        '''

        self._close = '''
    </body>
</html>
        '''
        self.animal = "The animal"
        self.css_url = "css/styles.css"
        self._title = "The Animals Page"
        self.__sound = "animal sound"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def css(self):
        return self.css_url

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())


