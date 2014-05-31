import json
import urllib2
class ApiModel(object):
    def __init__(self):
        self.url = "http://rebeccacarroll.com/api/music/music.json"
        self.array = []

    def send_request(self):
        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        jsondoc = json.load(data)

        self.all_items = jsondoc['songs']['track']

        #print self.all_items
        # self.__api_data.array = self.data_array

        self.array_length = len(self.all_items)
        #print self.array_length

        for item in self.all_items:
            self.__api_data = ApiDataObject()
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

            self.array.append(self.__api_data)

        #print self.array

        #print self.data_array

    #
    # @property
    # def data_parsed(self):
    #     return self.__api_data

class ApiDataObject(object):
    def __init__(self):
        self.file = ""
        self.title = ""
        self.artist = ""
        self.length = ""
        self.year = ""
        self.label = ""
        self.cover = ""
        self.all_items = ""
        self.array_length = ""




