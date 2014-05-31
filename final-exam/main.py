#Gabriel Ferraz
#DPW Final Exam
#05/30/2014
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

        api_view.api_array = api_model.array

        api_view.update()

        page.content = api_view.api_content

        if self.request.GET:
            request = self.request.GET['num']
            api_view.the_index = int(request)
            api_view.update2()
            page.api_content = api_view.api_new_content
            self.response.write(page.print_out())
        else:
            self.response.write(page.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
