from animals import Animals

class Fox(Animals):
    def __init__(self):
        #call constructor function
        Animals.__init__(self)
        self._title = "The Fox"
        self._animal = "FOX"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Carnivora"
        self._family = "Canidae"
        self._genus = "Vulpes"
        self._url = "http://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Fuzzy_Freddy.jpg/1200px-Fuzzy_Freddy.jpg"
        self._avg_lifespan = "5 years (In Wild)"
        self._habitat = "Wooded areas, prairies and farmland"
        self._geo_location = "Planet Earth"
        self._sound = "Scream-y howl"
        self._body_id = "fox"

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())
