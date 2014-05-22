from page import Page
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.number = 1



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
