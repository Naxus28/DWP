#libraries to work with json in python
import urllib2
import json

class FlickrModel(object):
    def __init__(self):

        #=============flickr.photos.getRecent API============
        #get the api info
        self.url = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=01b1c8d61f0ee804f95f20fe64fba996&format=json&extras=views&nojsoncallback=1"
        self.__flkrdata = ""

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


class FlickrDataObject(object):
    def __init__(self):
        self.farm = ""
        self.server = ""
        self.the_id = ""
        self.secret = ""
        self.the_urls = []
