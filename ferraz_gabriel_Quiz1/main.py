#function calc_area
def calc_area(w,h):
    if w == h:
        print "The width and height are the same. This is a square of: " + str(w * h) + " square feet"
    else:
        print "This is a rectangle of: " + str(w * h) + " square feet"
        return w * h

calc_area(20,20)
calc_area(10,4)
