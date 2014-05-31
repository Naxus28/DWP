import json
import urllib2
class ApiModel(object):
    def __init__(self):
        self.url = "http://rebeccacarroll.com/api/music/music.json"
        self.file = ""
        self.title = ""
        self.artist = ""
        self.length = ""
        self.year = ""
        self.label = ""
        self.cover = ""
        self.songs_array = ""

        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        jsondoc = json.load(data)

        #print jsondoc

        self.__api_data = ApiDataObject()

        all_items = jsondoc['songs']['track']

        # if not 'file' in all_items:
        #     print "files not found"
        # else:
        #     print "no files found"


        #print all_items[1]['title']
        #print all_items

        #length = len(all_items)
        #print length
        #
        for item in all_items:
            #print item
            if 'file' in item:
                self.__api_data.file = item['file']
            else:
                self.__api_data.file = "No item to display"

            if 'title' in item:
                self.__api_data.title = item['title']
            else:
                self.__api_data.title = "No item to display"

            if 'artist' in item:
                self.__api_data.artist = item['artist']
            else:
                self.__api_data.artist = "No item to display"

            if 'length' in item:
                self.__api_data.length = item['length']
            else:
                self.__api_data.length = "No item to display"

            if 'year' in item:
                self.__api_data.year = item['year']
            else:
                self.__api_data.year = "No item to display"

            if 'label' in item:
                self.__api_data.label = item['label']
            else:
                self.__api_data.label = "No item to display"

            if 'cover' in item:
                self.__api_data.cover = item['cover']
            else:
                self.__api_data.cover = "No item to display"

            print self.__api_data.artist
            print self.__api_data.title


    @property
    def data_parsed(self):
        return self.__api_data

class ApiDataObject(object):
    def __init__(self):
        self.file = ""
        self.title = ""
        self.artist = ""
        self.length = ""
        self.year = ""
        self.label = ""
        self.cover = ""



