#Gabriel Ferraz
#DPW Final Exam
#05/30/2014
from page import PageView
from model import ApiModel

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = PageView()
        api_model = ApiModel()
        #print api_model.url
        self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
