import json
import urllib2
class ApiModel(object):
    def __init__(self):
        self.url = "http://rebeccacarroll.com/api/music/music.json"
        self.mp3 = ""
        self.title = ""
        self.artist = ""
        self.length = ""
        self.year = ""
        self.label = ""
        self.image = ""

        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        jsondoc = json.load(data)

        #print jsondoc

        self.__api_data = ApiDataObject()

        self.__api_data.title = jsondoc['songs']['track'][0]['title']

        print self.__api_data.title

    @property
    def data_parsed(self):
        return self.__api_data

class ApiDataObject(object):
    def __init__(self):
        self.mp3 = ""
        self.title = ""
        self.artist = ""
        self.length = ""
        self.year = ""
        self.label = ""
        self.image = ""



