import math

#input fields down below
first_noun = raw_input('Please enter a noun:')
second_noun = raw_input('Please enter a verb:')
third_noun = raw_input('Please enter a yet another noun:')
fourth_noun = raw_input('Please enter a noun--again:')
first_integer = raw_input('Please enter an integer:')
second_integer = raw_input('Please enter an integer:')
third_integer = raw_input('Please enter another integer:')
fourth_integer = raw_input('Please enter the last integer:')


#if statements (last one has two logical operators),
#  mathematical operators, assignment operators,
if first_integer:
    first_integer = (int(first_integer) + 21)
    first_integer -= 3
else:
    first_integer = 1


if second_integer:
    second_integer = (int(second_integer) - 10)
    second_integer += 11
else:
    second_integer = 4


if third_integer and second_integer and first_integer:
    third_integer = (int(third_integer) * 2)
    third_integer /= 2
    if third_integer % 2 != 0:
        math.floor(third_integer)
else:
    third_integer = 10


#array and dictionary
array_noun = [first_noun,second_noun,third_noun,fourth_noun]

integer = {'integer_one': first_integer, 'integer_two':second_integer,'integer_three':third_integer}

new_integer = integer['integer_one']

#for loop
for i in range(0,2):
    array_noun = [array_noun[3],array_noun[0], array_noun[1],array_noun[2]]
   # print array_noun

#functions
def integer_calc(x,y,z):
    return x+y-z

function_one_result = integer_calc(integer['integer_one'],integer['integer_two'],integer['integer_three'])
#print function_one_result


def integer_calc_two(x,y,z):
    return x*y-z

function_two_result = integer_calc_two(first_integer,second_integer,third_integer)
#print function_two_result

message = '''
This is my {array_noun[3]} madlib experience!
I did some {array_noun[1]} on google to learn what a madlib is.
I looked up only {function_one_result} websites and got an {array_noun[2]} of what it is.
It took me about {new_integer} minutes to write this text.
Guess how long it took me to write the code... certainly not {fourth_integer} minutes. Maybe some {function_one_result} minutes.
Crazy, huh?
I hope you liked that your answers were all scrambled up and displayed in a different order than you entered them.
Don't we love coding? ;)
'''

message = message.format(**locals())
print message