class Animal(object):
    def __init__(self):
        self.__css_url = "css/styles.css"
        self.__title1 = "The Animals Page"
        self._title = ""
        self._font = "http://fonts.googleapis.com/css?family=Henny+Penny|Unkempt|Gloria+Hallelujah|Indie+Flower|Shadows+Into+Light|Droid+Serif"
        self._animal = "The animal"
        self._fox = ""
        self._phylum = ""
        self._class_ = ""
        self._order = ""
        self._family = ""
        self._genus = ""
        self._avg_lifespan = ""
        self._habitat = ""
        self._geo_location = ""
        self._sound = "animal sound"
        self._body_id = ""
        self._link = ""
        self._open = ""
        self._content = ""
        self._close = ""

    #function that returns the main title. It is protected and cannot be overwritten in another class
    #This is readable only because we are not changing it anywhere
    @property
    def main_title(self):
        return self.__title1

    #functions that 1)get and then 2)set the title for specific pages (i.e.The Rabbit).
    # This attribute is private, thus can be overwritten outside this class
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title


     #functions that 1)get and then 2)set the name of the animal for specific pages (i.e. Rabbit).
    # This attribute is private, thus can be overwritten outside this class
    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, new_animal):
        self._animal = new_animal

     #functions that 1)get and then 2)set the sound of the animal for specific pages (i.e. Honking).
    # This attribute is private, thus can be overwritten outside this class
    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, new_sound):
        self._sound = new_sound

    @property
    def css(self):
        return self.__css_url

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())


