import webapp2
from page import FormPage
from model import FlickrModel
from page import FlickrView

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        #=========data transfer for flickr.photos.getRecent API========
        flickr_model = FlickrModel()
        flickr_model.send_request()
        flickr_view = FlickrView()
        flickr_view.api_view = flickr_model.flkrdata
        flickr_view.update_api_view()
        view.page_content = flickr_view.api_content

        if self.request.GET:
            flickr_model2 = 
            api2 = self.


    self.response.write(view.print_out())




        # self.response.write(view.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)