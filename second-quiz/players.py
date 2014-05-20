class Player(object):
    def __init__(self):
        self.__title = "The Soccer Players App"
        self._name = ""
        self._position = ""
        self._speed = 0
        self._dribble = ""
        self._catch = ""
        self._team = ""
        self._salary = ""

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.__title + "</br>" + "Player Name: " + self._name +"</br>Player Position: " + self._position +\
                   "</br>Player Speed: " + str(self._speed) + "km/h" + "</br>Player Dribble Level: " + self._dribble + \
                   "</br>Player Catch Level: " + self._catch + str(self._salary) + "</br> </br>"