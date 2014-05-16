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

        f = Fox()
        w = Wolf()
        r = Rabbit()
        the_animals = [f, w, r]

        # print f.title
        # self.response.write(f.print_out())
        # self.response.write(r.print_out())
        # self.response.write(w.print_out())

        if self.request.GET:
            animal = self.request.GET["animal"]
            if animal == "fox":
                self.response.write(the_animals[0].print_out())
            elif animal == "wolf":
                self.response.write(the_animals[1].print_out())
            else:
                self.response.write(the_animals[2].print_out())
        else:
            self.response.write(the_animals[0].print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
