
import webapp2
from page import Page
from form import FormPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.title = "Inheritance - Abstraction"
        p.form_header ="New Form"
        p.css_url = "css/styles.css"
        self.response.write(p.print_out())

        p2 = FormPage()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
