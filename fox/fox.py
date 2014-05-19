from animals import Animal

class Fox(Animal):
    def __init__(self):
        #call constructor function
        Animal.__init__(self)
        self.title = "The Fox"
        self.animal = "FOX"
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

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())
