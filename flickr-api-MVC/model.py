#libraries to work with json in python
import urllib2
import json

class FlickrModel(object):
    def __init__(self):

        #=============flickr.photos.getRecent API and photos.Search API============
        #url for the first api - doesn't take user's input - returns most recent pictures
        self.url = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=01b1c8d61f0ee804f95f20fe64fba996&format=json&extras=views&nojsoncallback=1"
        self.__flkrdata = ""

        #url for the second api - this takes the user's input to build the URL string
        #  - returns pictures based on search term
        self.url2_one = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=01b1c8d61f0ee804f95f20fe64fba996&tags="
        self.url2_two = "&tag_mode=&text="
        self.url2_three = "&sort=interestingness-desc&content_type="
        self.url2_four ="&format=json&nojsoncallback=1"
        self.query = ""
        self.full_url2 = ""
        self.url_safe = ""
        self.__flkrdata2 = ""

    #function that requests and parses data from the API
    def send_request(self):
        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()

        #this is going to get the information
        data = opener.open(req)

        #parse the data
        jsondoc = json.load(data)

        #instantiates the object class that has the API data
        self.__flkrdata = FlickrDataObject()

        #array to hold the pictures returned
        self.__flkrdata.the_urls = []

        #loop through the pictures and get the necessary info to "build" 40 pictures
        for photo in range(0, 50):
            self.__flkrdata.farm = jsondoc['photos']['photo'][photo]['farm']
            self.__flkrdata.server = jsondoc['photos']['photo'][photo]['server']
            self.__flkrdata.the_id = jsondoc['photos']['photo'][photo]['id']
            self.__flkrdata.secret = jsondoc['photos']['photo'][photo]['secret']

            #append the pictures to the array
            self.__flkrdata.the_urls.append("http://farm"+str(self.__flkrdata.farm)+".staticflickr.com/"+str(self.__flkrdata.server)+"/"
                            + str(self.__flkrdata.the_id)+"_"+str(self.__flkrdata.secret)+".jpg")

    @property
    def flkrdata(self):
        return self.__flkrdata


    #=============flickr.photos.Search API============
    def send_request2(self):
        self.full_url2 = self.url2_one + self.query + self.url2_two + self.query + self.url2_three + self.query \
            + self.url2_four

        self.url_safe = self.full_url2.replace(" ", "%20")

        req = urllib2.Request(self.url_safe)
        opener = urllib2.build_opener()
        #this is going to get the information for us
        data = opener.open(req)

        #parse the returned data
        jsondoc = json.load(data)

        #instantiates the object class that has the API data
        self.__flkrdata2 = FlickrDataObject2()

       #array that holds the pictures URLs
        self.__flkrdata2.the_search_urls = []

        #array that holds users URL
        self.__flkrdata2.users_urls = []

        #creates another instance of the query to create a ling to the searched topic on Flickr
        self.__flkrdata2.query = self.query
        print self.__flkrdata2.query

         #loop through the pictures and get the necessary info to "build" 20 pictures
        for photo in range(0, 100):
            self.__flkrdata2.farm = jsondoc['photos']['photo'][photo]['farm']
            self.__flkrdata2.server = jsondoc['photos']['photo'][photo]['server']
            self.__flkrdata2.the_id = jsondoc['photos']['photo'][photo]['id']
            self.__flkrdata2.secret = jsondoc['photos']['photo'][photo]['secret']
            self.__flkrdata2.owner = jsondoc['photos']['photo'][photo]['owner']

            #append picuture urls to the array
            self.__flkrdata2.the_search_urls.append("http://farm"+str(self.__flkrdata2.farm)+".staticflickr.com/"+str(self.__flkrdata2.server)+"/"+
                                           str(self.__flkrdata2.the_id)+"_"+str(self.__flkrdata2.secret)+".jpg")

            #append users urls to the array
            self.__flkrdata2.users_urls.append("https://www.flickr.com/people/"+self.__flkrdata2.owner)

            #lenght of the pictures array to be updated according to the number of pictures displayed
            self.__flkrdata2.picture_array_length = str(len(self.__flkrdata2.the_search_urls))


    @property
    def flkrdata2(self):
        return self.__flkrdata2

#============objects that hold the APIs data=========
#flickr.photos.getRecent API
class FlickrDataObject(object):
    def __init__(self):
        self.farm = ""
        self.server = ""
        self.the_id = ""
        self.secret = ""
        self.the_urls = []

#flickr.photos.Search API
class FlickrDataObject2(object):
    def __init__(self):
        self.farm = ""
        self.server = ""
        self.the_id = ""
        self.secret = ""
        self.the_search_urls = []
        self.users_urls = []
        self.picture_array_length = ""