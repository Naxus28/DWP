from animals import Animals

class Wolf(Animals):
    def __init__(self):
        #call constructor function
        Animals.__init__(self)
        self._title = "The Grey Wolf"
        self._animal = "GREY WOLF"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Carnivora"
        self._family = "Canidae"
        self._genus = "	Canis"
        self._url = "http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wolf%2C_voor_de_natuur%2C_Saxifraga_-_Jan_Nijendijk.5097.jpg/1014px-Wolf%2C_voor_de_natuur%2C_Saxifraga_-_Jan_Nijendijk.5097.jpg"
        self._avg_lifespan = "5 years (In Wild)"
        self._habitat = "Deserts, grasslands, forests and arctic tundras."
        self._geo_location = "North America and Europe"

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())