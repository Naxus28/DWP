import math

#input fields down below
first_noun = raw_input('Please enter a noun:')
second_noun = raw_input('Please enter another noun:')
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

