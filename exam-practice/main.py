from page import PageView
from model import ApiModel
from page import ApiView

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = PageView()
        api_model = ApiModel()
        api_view = ApiView()

        api_model.send_request()

        api_view.data_view = api_model.data_parsed
        api_view.update()
        page.page_content = api_view.api_content
        self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
