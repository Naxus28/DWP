import webapp2
from page import Page
from page import FormPage

#libraries for working with xml in python
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.form_header = "Flickr API Test"

        #if there are URL variables...
        if self.request.GET:
            code = self.request.GET['code']
        #go get the api info
            url = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=01b1c8d61f0ee804f95f20fe64fba996&per_page=1&page=1&format=json&nojsoncallback=1&auth_token=72157644801259232-2c7f65d8e28f81f1&api_sig=c73b458ca63066107d45f80dc5f494e7"
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            #this is going to get the information for us
            data = opener.open(req)
        #parse it
            jsondoc = json.load(data)
            content = jsondoc['photos']
            view.page_content = content
            # fahrenheit = 1.8*(content-273)
            # view.page_content += "</br> Temperature in Fahrenheit: " + str(fahrenheit)
            # view.page_content += "</br> Temperature in Celcius: " + str((fahrenheit-32)*5/9)

            #print jsondoc['coord']

            print content
            self.response.write(content)

        #print out
        self.response.write(view.print_out())



        #look at elements within it

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
