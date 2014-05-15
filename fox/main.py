# Name: Gabriel Ferraz
# Date: 05/14/2014
# Assignment: What does the Fox say?

#
import webapp2
from fox import Fox
from rabbit import Rabbit
from wolf import Wolf




class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')

        w = Wolf()
        r = Rabbit()
        f = Fox()

        # the_animals = [w, r, f]
        print f.title
        self.response.write(f.print_out())
        self.response.write(r.print_out())
        self.response.write(w.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
