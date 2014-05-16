class Animals(object):
    def __init__(self):

        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.main_title} | {self.title}</title>
        <link rel="stylesheet" type="text/css" href={self.css}>
        <link href={self._font} rel="stylesheet" type="text/css">
        <script src="js/modernizr.2.5.3.min.js"></script>

    </head>
    <header>
        <h1>The Animals Page</h1>
        <nav>
            <ul>
                <li><a href="?animal=fox">FOX</a></li>
                <li><a href="?animal=wolf">WOLF</a></li>
                <li><a href="?animal=rabbit">RABBIT</a></li>
            </ul>
        </nav>
    </header>
    <body id="{self._body_id}">
        '''
        self._content = '''
        </div>
        <div id="info">
            <h2>Information about the {self.animal}</h2>
            <p><span>Phylum:</span> {self._phylum}</p>
            <p><span>Class:</span> {self._class_}</p>
            <p><span>Order:</span> {self._order}</p>
            <p><span>Family:</span> {self._family}</p>
            <p><span>Genus:</span> {self._genus}</p>
            <p><span>Average Life Span:</span> {self._avg_lifespan}</p>
            <p><span>Habitat:</span> {self._habitat}</p>
            <p><span>Geo Location:</span> {self._geo_location}</p>
             <p><span>Typical sound emitted:</span> {self._sound}</p>
        </div>
        <div id ="image">
            <h2 id="animal_image">This is the {self.animal}</h2>
            <figure>
                <img id ="the_fox" src="{self._fox}" alt="{self.animal}">
                <img id ="the_image" src="{self._url}" alt="{self.animal}">
                <figcaption>Original image can be found at <a href ="{self._url}" target="_blank">{self._link}</a></figcaption>
            </figure>
        </div>
        '''

        self._close = '''
        <script src="js/jquery-1.11.0.min.js"></script>
        <script src="js/initial.js"></script>
    </body>
</html>
        '''
        self._font = "http://fonts.googleapis.com/css?family=Henny+Penny|Unkempt|Gloria+Hallelujah|Indie+Flower|Shadows+Into+Light"
        self._animal = "The animal"
        self._fox = ""
        self.css_url = "css/styles.css"
        self.__title1 = "The Animals Page"
        self._title = ""
        self._sound = "animal sound"
        self._body_id = ""
        self._link = ""

    @property
    def main_title(self):
        return self.__title1

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


