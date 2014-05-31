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
        self.songs_array = ""

        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        jsondoc = json.load(data)

        #print jsondoc

        self.__api_data = ApiDataObject()

        all_items = jsondoc['songs']['track']

        print all_items[1]['title']
        #print all_items

        length = len(all_items)
        print length

        for item in all_items:
            #print item
            self.__api_data.title = item['title']
            if not item['title']:
                item['title'] = "No item to display"


            self.__api_data.artist =

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



