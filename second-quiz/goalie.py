from players import Player

class Goalie(Player):
    def __init__(self):
        Player.__init__(self)
        self._name = "Charlie the Goalie"
        self._position = "Goalie"
        self._speed = 3
        self._dribble = "Bad Dribbler"
        self._catch = "Great Keeper"
        self._team = "Real Madrid"
        self._salary = 80

def update(self):
        self.all = "</br>" + "Player Name: " + self._name +"</br>Player Position: " + self._position +\
                   "</br>Player Speed: " + str(self._speed) + "km/h" + "</br>Player Dribble Level: " + self._dribble + \
                   "</br>Player Catch Level: " + self._catch + "</br>" + self._team + "</br> Salary: " + self._salary +\
                   "</br>"