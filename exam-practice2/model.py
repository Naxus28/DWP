import json
import urllib2
from xml.dom import minidom
class ApiModel(object):
    def __init__(self):
        self.url = "http://xml.weather.yahoo.com/forecastrss?p=32792"
        self.country = ""
        self.weather = ""
        self.description = ""
        self.temp = ""
        self.api_data = ""

    def send_request(self):
        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        #jsondoc = json.load(data)
        minidomdoc = minidom.parse(data)

        self.api_data = ApiDataObject()

        the_country = minidomdoc.getElementsByTagName('yweather:location')[0]
        the_description = minidomdoc.getElementsByTagName('description')[0].firstChild.nodeValue
        the_condition = minidomdoc.getElementsByTagName('yweather:condition')[0]


        print the_country

        self.api_data.country = the_country.attributes['country'].value
        self.api_data.description = the_description
        self.api_data.weather = the_condition.attributes['temp'].value

        print self.api_data.country

        #self.api_data.weather = minidomdoc.getElementsByTagName('yweather:condition').attribute['temp'].value
        #self.api_data.description = minidomdoc.getElementsByTagName('yweather:description')[0]
        #self.api_data.weather = minidomdoc.getElementsByTagName('yweather:condition').attribute['temp'].value


        #
        # self.api_data.country = jsondoc['sys']['country']
        # self.api_data.weather = jsondoc['weather'][0]['main']
        # self.api_data.description = jsondoc['weather'][0]['description']
        # self.api_data.temp = jsondoc['main']['temp']

    @property
    def parsed_data(self):
        return self.api_data

class ApiDataObject(object):
    def __init__(self):
        self.country = ""
        self.weather = ""
        self.description = ""
        self.temp = ""

        print self.country