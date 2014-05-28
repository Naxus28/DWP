import webapp2
from page import FormPage
from model import FlickrModel
from page import FlickrView
from page import FlickrView2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        #=========data transfer for flickr.photos.getRecent API========
        flickr_model = FlickrModel()
        flickr_model.send_request()
        flickr_view = FlickrView()
        flickr_view.api_view = flickr_model.flkrdata
        #print flickr_view.api_view
        flickr_view.update_api_view()
        view.page_content = flickr_view.api_content

        #=========data transfer for flickr.photos.Search API========
        if self.request.GET:
            flickr_model2 = FlickrModel()
            flickr_model2.query = self.request.GET['query']
            if flickr_model2.query == "":

                self.response.write(view.print_out())
            else:
                view.arrow = "<img id = 'arrow' src = 'images/arrow1.png'/>"
                flickr_model2.send_request2()
                flickr_view2 = FlickrView2()
                flickr_view2.api_view2 = flickr_model2.flkrdata2
                flickr_view2.update_api_view2()
                view.searched_pictures = flickr_view2.full_content

        self.response.write(view.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)