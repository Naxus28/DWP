from animals import Animals

class Rabbit(Animals):
    def __init__(self):
        #call constructor function
        Animals.__init__(self)
        self._title = "The Rabbit"
        self._animal = "RABBIT"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Lagomorpha"
        self._family = "Leporidae"
        self._genus = "Sylvilagus"
        self._url = "http://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Rabbit_in_montana.jpg/1013px-Rabbit_in_montana.jpg"
        self._avg_lifespan = "9 to 12 years"
        self._habitat = "Meadows, woods, forests, grasslands, deserts and wetlands."
        self._geo_location = "Planet Earth"

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())
