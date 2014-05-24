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

        #=============flickr.photos.getRecent API============
        #get the api info
        url = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=01b1c8d61f0ee804f95f20fe64fba996&format=json&nojsoncallback=1"
        req = urllib2.Request(url)
        opener = urllib2.build_opener()

        #this is going to get the information
        data = opener.open(req)

        #array to hold the pictures returned
        the_urls = []

        #parse the data
        jsondoc = json.load(data)

        #loop through the pictures and get the necessary info to "build" 40 pictures
        for photo in range(0, 40):
            farm = jsondoc['photos']['photo'][photo]['farm']
            server = jsondoc['photos']['photo'][photo]['server']
            the_id = jsondoc['photos']['photo'][photo]['id']
            secret = jsondoc['photos']['photo'][photo]['secret']
            #append the pictures to the array
            the_urls.append("http://farm"+str(farm)+".staticflickr.com/"+str(server)+"/"+str(the_id)+"_"+str(secret)+".jpg")

        #push the pictures to the view
        for the_url in range(0, 40):
            view.page_content += "<div class='img-container'><a href='"+the_urls[the_url]+"'><img src ='"+the_urls[the_url]+"'></a></div>"

        #print view.page_content


        #=============flickr.photos.search API============
        #API web page: https://www.flickr.com/services/api/explore/flickr.photos.search
        #This is what the json file looks like (only one object in the array for this example):
    #     { "photos": { "page": 1, "pages": "527848", "perpage": 100, "total": "52784744",
    #           "photo": [
    #                    { "id": "14072114588", "owner": "107424305@N06", "secret": "2416c1e0b4",
    #  "server": "3674", "farm": 4, "title": "Mi avistamiento de Flash (en moto) - Flash in Motorcycle",
    # "ispublic": 1, "isfriend": 0, "isfamily": 0 }
                          #  ]}

         #if there is an input
        if self.request.GET:
            query = self.request.GET['query']
            #get the api info
            url= "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=01b1c8d61f0ee804f95f20fe64fba996&tags="+query+"&text="+query+"&content_type="+query+"&format=json&nojsoncallback=1&auth_token=72157644817258645-6445e7bd8ad6d5c9&api_sig=092c8362a74e4bed99152093fe3b36b0"
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            #this is going to get the information for us
            data = opener.open(req)

            #parse the returned data
            jsondoc = json.load(data)
            #farm = jsondoc['photos']
            print jsondoc

            # print url_search
            # #loop through the pictures and get the necessary info to "build" 20 pictures
            # for photo in range(0, 20):
            #     the_search_urls = []
            #     farm = jsondoc['photos']['photo'][photo]['farm']
            #     server= jsondoc['photos']['photo'][photo]['server']
            #     the_id= jsondoc['photos']['photo'][photo]['id']
            #     secret = jsondoc['photos']['photo'][photo]['secret']
            #     the_search_urls.append("http://farm"+str(farm_one)+".staticflickr.com/"+str(server_one)+"/"+
            #                            str(the_id_one)+"_"+str(secret_one)+".jpg")
            #     print the_search_urls
            #
            # for the_search_url in range(0, 20):
            #     view.searched_pictures += "<div class='searched-img-container'><a href='"+the_search_urls[the_search_url]+"'><img src ='"+the_search_urls[the_search_url]+"'></a></div>"
            #
            # print view.searched_pictures





        self.response.write(view.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
