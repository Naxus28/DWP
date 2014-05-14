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