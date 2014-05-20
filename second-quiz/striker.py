from players import Player

class Striker(Player):
    def __init__(self):
        Player.__init__(self)
        self._name = "James Striker"
        self._age = 29
        self._position = "Attack"
        self._speed = 6
        self._dribble = "Super Dribbler"
        self._catch = "Can't put his hands on the ball"
        self._titles = "Five Times World Champion"


def update(self):
        self.all = "</br>" + "Player Name: " + self._name + "</br>Player Age: " + str(self._age) + \
                   "</br>Player Position: " + self._position + "</br>Player Speed: " + str(self._speed) + "km/h" +\
                   "</br>Player Dribble Level: " + self._dribble + "</br>Player Catch Level: " + self._catch +\
                   "</br>" + self._titles + "</br>"