import webapp2
from page import Page
from page import FormPage

#libraries for working with xml in python
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.form_header = ""

        #if there are URL variables...
        if self.request.GET:
            query = self.request.GET['query']
            #go get the api info
            url_search =  "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=922fd10874987e031bb23715c945c8de&tags="+query+"&text="+query+"&content_type="+query+"&format=json&nojsoncallback=1&auth_token=72157644817258645-6445e7bd8ad6d5c9&api_sig=092c8362a74e4bed99152093fe3b36b0"
            req_one = urllib2.Request(url_search)
            opener_one = urllib2.build_opener()
            #this is going to get the information for us
            data_one = opener_one.open(req_one)
            #parse it
            jsondoc_one = json.load(data_one)
        for photo in range(0, 40):
            farm = jsondoc['photos']['photo'][photo]['farm']
            server = jsondoc['photos']['photo'][photo]['server']
            the_id = jsondoc['photos']['photo'][photo]['id']
            secret = jsondoc['photos']['photo'][photo]['secret']

        #get the api info
        url = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=84c81a688848153a0fa4db04702b63fd&format=json&nojsoncallback=1"
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        #this is going to get the information for us
        data = opener.open(req)
        #parse it

        the_urls = []

        jsondoc = json.load(data)
        for photo in range(0, 40):
            farm = jsondoc['photos']['photo'][photo]['farm']
            server = jsondoc['photos']['photo'][photo]['server']
            the_id = jsondoc['photos']['photo'][photo]['id']
            secret = jsondoc['photos']['photo'][photo]['secret']

            the_urls.append("http://farm"+str(farm)+".staticflickr.com/"+str(server)+"/"+str(the_id)+"_"+str(secret)+".jpg")

        for the_url in range(0, 40):
            view.page_content += "<div class='img-container'><a href='"+ the_urls[the_url] + "'><img src ='"+the_urls[the_url]+"'></a></div>"

        #print view.page_content

        self.response.write(view.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
