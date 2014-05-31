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

            # if not 'file' in all_items:
            #     self.__api_data.file = "No item to display"
            # else:
            #     self.__api_data.file = item['file']

            # self.__api_data.title = item['title']
            # if not item['title']:
            #     item['title'] = "No item to display"
            #
            # self.__api_data.artist = item['artist']
            # if not item['artist']:
            #     item['artist'] = "No item to display"
            #
            # self.__api_data.length = item['length']
            # if not item['length']:
            #     item['length'] = "No item to display"
            #
            # self.__api_data.year = item['year']
            # if not item['year']:
            #     item['year'] = "No item to display"
            #
            # self.__api_data.label = item['label']
            # if not item['label']:
            #     item['label'] = "No item to display"
            #
            # self.__api_data.cover = item['cover']
            # if not item['cover']:
            #     item['cover'] = "No item to display"

            print self.__api_data.file

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



