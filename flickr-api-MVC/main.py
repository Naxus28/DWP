import webapp2
from page import Page
from page import FormPage
from model import FlickrModel
from page import FlickrView

#libraries for working with xml in python

# import urllib2
# import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        api_view = FlickrView()
        print api_view

         #if there is an input
        if self.request.GET:
            query = self.request.GET['query']
            if query == "":
                self.response.write(view.print_out())
            else:
                #get the api info
                url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=01b1c8d61f0ee804f95f20fe64fba996&tags="+query+"&tag_mode=&text="+query+"&sort=interestingness-desc&content_type="+query+"&format=json&nojsoncallback=1"

                url_safe = url.replace(" ", "%20")

                req = urllib2.Request(url_safe)
                opener = urllib2.build_opener()
                #this is going to get the information for us
                data = opener.open(req)

                #parse the returned data
                jsondoc = json.load(data)

                #array that holds the pictures URLs
                the_search_urls = []

                #array that holds users URL
                users_urls = []

                #loop through the pictures and get the necessary info to "build" 20 pictures
                for photo in range(0, 100):
                    farm = jsondoc['photos']['photo'][photo]['farm']
                    server = jsondoc['photos']['photo'][photo]['server']
                    the_id = jsondoc['photos']['photo'][photo]['id']
                    secret = jsondoc['photos']['photo'][photo]['secret']
                    owner = jsondoc['photos']['photo'][photo]['owner']
                    the_search_urls.append("http://farm"+str(farm)+".staticflickr.com/"+str(server)+"/"+
                                           str(the_id)+"_"+str(secret)+".jpg")
                    users_urls.append("https://www.flickr.com/people/"+owner)
                    print the_search_urls

                #lenght of the array
                array_length = len(the_search_urls)
                #H2 for the search results, displaying the number of pictures that is generated dynamically
                view.search_header_update = "<h2>Search Result: %s pictures" % array_length + "<span id='more_pics'> \
                                             (for more pictures on this topic, visit <a href= 'https://www.flickr.com/search/?q=%s' target = '_blank'>Flickr.com</a>)</span></h2>" % query
                view.arrow_up = "<img id = 'arrow' src = 'images/arrow1.png'/>"

                for the_search_url in range(0, 100):
                    view.searched_pictures += '''
                        <div class='picture_container'>
                            <div class='new_pictures'>
                                <a href='''+the_search_urls[the_search_url]+''' target='_blank'><img src ='''+the_search_urls[the_search_url]+'''></a>"
                                <div id='users'>
                                    <a href='''+users_urls[the_search_url]+''' target='_blank'>Photographer's Flickr Profile</a>
                                </div>
                            </div>
                        </div>
                        '''

        self.response.write(view.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)