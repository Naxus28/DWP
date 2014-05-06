#comments - single line comment uses the hash tag

'''
Gabriel Ferraz
05.05.14
DPW
'''

#print "Hello World"

first_name = "Gabriel"

last_name = "Ferraz"

print first_name +" "+  last_name

year_born = 1977
age = 2014 - year_born



age +=1 #adds one to the age

print age

#age++ # doesn't exist in python

#ASSIGNMENT OPERATORS
# assignment operators that are used in python: -= += *= /=


#CONDITIONALS

if year_born < 1990:
    print 'you are part of generation x'
    print 'you are part of generation y'

#the spacing is necessary and it has to be consistent
#no parenthesis or curly braces are necessary


if year_born < 1990:
    print 'you are part of generation x'
else:
    print 'you are part a millennial'

#if we want to structure the code but dont have anything to put in there yet--like in an if else statement--, we use
#  the word pass and the line is disregarded:
#i.e.

# if year_born < 1990:
#     print 'you are part of generation x'
# else:
#     pass

#elif is else if put together
if year_born > 1995:
    print 'you are part of millennial generation'
elif year_born > 1978:
    print 'you are part of generation y'
elif year_born > 1965:
    print 'you are part of generation x'
else:
    print 'these generations don not apply'

#ARRAYS
students = ['Nicole','Eli','Gabriel','Jordan','Danny', 'kkkkk','lllll']

students.append('Arturo')
print students

#DICTIONARIES - ASSOCIATIVE ARRAYS
#name_of_dict = {'key': value}
class_info = {'students': students, 'roster count': 9, 'room':'FS4A7'}
print 'this is the key room '+ class_info['room']

#LOOPS - in python loops are naturally for each

for s in students:
    print s + ' you will do great in this class'
    if s == 'Eli':
        break
#for i in range (start, end, increment/decrement)
for i in range(0,8):
    print students[i]

#rabdn numbers

import random

for i in range(0,10):
    print random.randrange(20)

#FUNCTIONS
def calc_area(h,w):
    area = h*w
    print area

calc_area(200,300)

#use return and hold the value

def calc_area(h,w):
    area=h*w
    return area

a = calc_area(200,300)

print a

#FORMAT STRING METHODS
user_name = 'Kermit'
join_date = 2001
message = '''
Welcome to our site, {user_name}!
It is great that you are here! You have been with us since {join_date}!
'''

message = message.format(**locals())
# print message

first_name = raw_input('Type your first name:')
print first_name + ', nice to meet you.'

#raw input expects a string; if we use integers, we need to tell python to
#interpret the input as an integer

age = raw_input('Type your age:')
print str(int(age)+2) + ' is your age'
