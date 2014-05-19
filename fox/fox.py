from animals import Animal
from html import Html

class Fox(Animal, Html):
    def __init__(self):
        #call constructor function
        Animal.__init__(self)
        Html.__init__(self)
        #the property below is just a test to make sure my main stylesheet was protected
        self.__css_url = ""

        self._title = "The Fox"
        self._animal = "FOX"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Carnivora"
        self._family = "Canidae"
        self._genus = "Vulpes"
        self._url = "images/fox-4.png"
        self._fox = "images/megan_fox.jpeg"
        self._avg_lifespan = "5 years (In Wild)"
        self._habitat = "Wooded areas, prairies and farmland"
        self._geo_location = "Planet Earth"
        self.sound = "Scream-y howl"
        self._body_id = "fox"
        self._link = "flickr.com"

    #this is the polymorphic function. It updates the html for every different animal and
    # overwrites the following super class functions: title(), animal(), and sound()
    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())
