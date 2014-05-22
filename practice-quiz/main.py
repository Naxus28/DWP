from page import Page
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        if self.request.GET:
            count = self.request.GET['name']
            if count == "the_function":
                p.number = 1
                self.response.write(p.print_out())
            else:
                self.response.write(p.print_out())
        else:
            self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
