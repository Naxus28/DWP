#function calc_area
def calc_area(w,h):
    if w == h:
        print "The width and height are the same. This is a square of: " + str(w * h) + " square feet"
    else:
        print "This is a rectangle of: " + str(w * h) + " square feet"
        return w * h

calc_area(20,20)
calc_area(10,4)

#function count down
def count_down(count):
    for i in range(count):
        print str(count) + " Bottles on the wall. " + str(count) + " Bottles of beer." \
                                             " Take one down and pass it around. Now you have " + str(count-1) + " bottles of beer on the wall."
        count -= 1
count_down(20)