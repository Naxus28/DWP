#Gabriel Ferraz
#DPW Final Exam
#05/30/2014
from page import PageView

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = PageView()
        self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
