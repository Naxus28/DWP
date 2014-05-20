class Player(object):
    def __init__(self):
        self.__title = "The Soccer Players App"
        self._name = ""
        self._position = ""
        self._speed = 0
        self._dribble = ""
        self._catch = ""
        self._team = " This player doesn't have this information"
        self._salary = " This player doesn't Have this information"
        self._team = " This player doesn't have this information"
        self._titles = " This player doesn't have this information"
        self._age = " This player doesn't have this information"

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.__title + "</br>" + "Player Name: " + self._name +"</br>Player Position: " + self._position +\
                   "</br>Player Speed: " + str(self._speed) + "km/h" + "</br>Player Dribble Level: " + self._dribble + \
                   "</br>Player Catch Level: " + self._catch + "</br>This is the salary:" + str(self._salary) +\
                   "</br>This is the team:" + self._team + "</br>This is the number of titles:" + str(self._titles) +\
                   "</br>This is the age: " + str(self._age)+ "</br> </br>"