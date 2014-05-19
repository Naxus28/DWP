import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
the_cal = cal.formatmonth(2013, 1, 0, 0)

#print the_cal

html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
the_html_cal = html_cal.formatmonth(2013, 1)

#print the_html_cal

# for i in cal.itermonthdays(2014,5):
#     print i
#
# for month in calendar.month_name:
#     print month
#
# for day in calendar.day_name:
#     print day

for m in range(1, 13):
    #print m
    cal = calendar.monthcalendar(2013, m)

    week_one = cal[0]
    week_two = cal[1]

    if week_one[calendar.FRIDAY] != 0:
        meet_day = week_one[calendar.FRIDAY]
    else:
        meet_day = week_two[calendar.FRIDAY]

    print "%10s %2d" % (calendar.month_name[m], meet_day)
    # print cal

# cal1 = calendar.monthcalendar(2013, 2)
# print cal1


#WATCH: https://www.youtube.com/watch?v=fVon4QaY4wo
#===============
def add_one(function, function1):
    def add_one_inside():
        return function() + function1()
    return add_one_inside


def func():
    return 3*2


def func1():
    return 5*2

the_func = add_one(func, func1)

print the_func()

#===============
def addThree(function, function1, function2):
    def addThreeInside():
        return function() + function1()*function2()
    return addThreeInside

def func():
    return 5+2

def func1():
    return 5*2

def func2():
    return 5-2

the_func1 = addThree(func, func1, func2)

print the_func1()


#===============
def addFunc(func):
    def innerAddFunc():
        return func() + 4
    return innerAddFunc

@addFunc
def func():
    return 5*3

@addFunc
def func1():
    return 3*8

def func2():
    return 5

print func()
print func1()

the_func = addFunc(func1)

print the_func()

#==========
def addFunc(func):
    def innerAddFunc(*args, **kwargs):
        return func(*args, **kwargs) + 4
    return innerAddFunc

@addFunc
def func(x=23):
    return 5*3 + x

@addFunc
def func1(y=76):
    return 3*8 + y


print func()
print func1(0)

the_func = addFunc(func1)

print the_func(10)

#===============
def a_func(func):
    def a_inside():
        return func()
    return a_inside

def main():
    a = "another a string"
    return a

the_func = a_func(main)
print the_func()

#============
def outer(y):
    x = y
    def inner(w):
        return y + x - w
    print inner(10)
outer(10)

#===========
def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def apply(function, a, b):
    return function(b, a)


print apply(add, 5, 4)

print apply(subtract, 5, 4)


class Pet:
    number_of_legs = 4
    def sleep(self):
        return "zzzzzzzzz"
    def pet_legs(self, new_number):
        return self.number_of_legs + new_number
    def pet_legs2(self, new_legs):
        print new_legs



dog = Pet()
#print "Doug has %s legs." % doug.number_of_legs
print dog.sleep()
print dog.pet_legs(0)

bird = Pet()
print "Birds have %s legs." % bird.pet_legs(-2)
#bird.number_of_legs = 2
print "new number of birds legs is %s" % bird.pet_legs(3)
bird.pet_legs2(3)


class player():
    age = 0
    legs = 2
    speed = 0
    ability = 0
    quality = 0
    weight = 0
    def player_speed(self, player_age, player_speed, player_weight, player_ability):
        if player_age >= 30:
            self.quality = player_age + player_speed*player_weight + player_ability
            return self.quality
        else:
            self.quality = player_age + player_speed*player_weight + player_ability
            return self.quality

Joe = player()
print "This is Joe's overall quality as a field player is: %s" % Joe.player_speed(30, 0.3, 180, 5)

Schmo = player()
print "This is Schmo's overall quality as a field player is: %s" % Schmo.player_speed(23, 0.5, 165, 3)


class goalie(player):
    def special_permission(self):
        return "can touch the ball with his hands"
    def field_ability(self):
        return self.player_speed(23, .13, 190, 1)
    def keeper_ability(self, jump, stretch, anticipation):
        return jump + stretch + anticipation



Charlie_the_goalie = goalie()
print "Charlie " + Charlie_the_goalie.special_permission()

print "Charlie' ability as a field player sucks. It is %s pts." % Charlie_the_goalie.field_ability() + \
      " However, his ability as a goalie is great: %s pts. The average is 195 pts." % Charlie_the_goalie.keeper_ability(20, 180, 15)
