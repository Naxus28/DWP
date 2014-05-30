import urllib2
import json
class ApiModel(object):
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q=32792"
        self.temp = ""
        self.temp_min = ""
        self.temp_max = ""
        self.humidity = ""
        self.wind_speed = ""
        self.__api_data = ""
        #print self.url

    def send_request(self):
        #print self.url
        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        jsondoc = json.load(data)
        print "in the request"

        self.__api_data = ApiDataObject()

        #print self.__api_data

        self.__api_data.temp = jsondoc['main']['temp']
        self.__api_data.temp_min = jsondoc['main']['temp_min']
        self.__api_data.temp_max = jsondoc['main']['temp_max']
        self.__api_data.humidity = jsondoc['main']['humidity']
        self.__api_data.wind_speed = jsondoc['wind']['speed']

        #print self.__api_data.temp

    @property
    def data_parsed(self):
        return self.__api_data


class ApiDataObject(object):
    def __init__(self):
        self.temp = "10"
        self.temp_min = "20"
        self.temp_max = "30"
        self.humidity = ""
        self.wind_speed = ""

        #print self.temp