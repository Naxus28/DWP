from page import Counter
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Counter()
        i = 1
        if self.request.GET:
            count = self.request.GET['name']
            if count == "the_function":

                p.number = i
                #i = i + 1
                self.response.write(p.print_out())
            else:
                self.response.write(p.print_out())
        else:
            self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
