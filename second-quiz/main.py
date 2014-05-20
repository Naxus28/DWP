# Gabriel Ferraz
# 05/19/2014
# Second Quiz
#
import webapp2
from striker import Striker
from goalie import Goalie

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write
        s = Striker()
        print s.print_out()

        g = Goalie()
        print g.print_out()

        content = s.print_out() + g.print_out()

        self.response.write(s.print_out())
        self.response.write(g.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
