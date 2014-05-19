from animals import Animal

class Rabbit(Animal):
    def __init__(self):
        #call constructor function
        Animal.__init__(self)
        self.title = "The Rabbit"
        self.animal = "RABBIT"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Lagomorpha"
        self._family = "Leporidae"
        self._genus = "Sylvilagus"
        self._url = "http://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Rabbit_in_montana.jpg/1013px-Rabbit_in_montana.jpg"
        self._fox = ""
        self._avg_lifespan = "9 to 12 years"
        self._habitat = "Meadows, woods, forests, grasslands, deserts and wetlands."
        self._geo_location = "Planet Earth"
        self.sound = "Honking"
        self._body_id = "rabbit"
        self._link = "wikimedia.com"

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())
