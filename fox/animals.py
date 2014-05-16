class Animals(object):
    def __init__(self):

        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href={self.css_url}>
        <link href={self.__font} rel="stylesheet" type="text/css">
    </head>
    <header>
        <h1>The Animals Page</h1>
    </header>
    <body>
        '''
        self._content = '''
        <div id="form">
           <a href="?animal=fox">FOX</a>
            <a href="?animal=wolf">WOLF</a>
            <a href="?animal=rabbit">RABBIT</a>
        </div>
        <div id="info">
            <h2>This is the {self.animal}</h2>
            <p>Phylum: {self._phylum}</p>
            <p>Class: {self._class_}</p>
            <p>Order: {self._order}</p>
            <p>Family: {self._family}</p>
            <p>Genus: {self._genus}</p>
            <p>Average Life Span: {self._avg_lifespan}</p>
            <p>Habitat: {self._habitat}</p>
            <p>Geo Location: {self._geo_location}</p>
            <figure>
                <img src="{self._url}" alt="{self.animal}">
                <figcaption>This image was taken from: {self._url}</figcaption>
            </figure>
        </div>
        '''

        self._close = '''
    </body>
</html>
        '''
        self.__font = "http://fonts.googleapis.com/css?family=Lato|Raleway"
        self._animal = "The animal"
        self.css_url = "css/styles.css"
        self._title = "The Animals Page"
        self._sound = "animal sound"
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, new_animal):
        self._animal = new_animal

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, new_sound):
        self._sound = new_sound

    @property
    def css(self):
        return self.css_url

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())


