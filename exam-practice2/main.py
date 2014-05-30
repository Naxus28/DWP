import webapp2
from page import PageView
from page import ApiView
from model import ApiModel

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = PageView()
        api_view = ApiView()
        api_model = ApiModel()
        api_model.send_request()
        api_view.view_data = api_model.parsed_data
        api_view.update()
        print api_view.api_content
        print page.content
        page.content = api_view.api_content

        self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
