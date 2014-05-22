import urllib2
from xml.dom import minidom

class WeatherModel(object):
    ''' This class handles data requests and sorting of data from the API '''
    def __init__(self):
            self.url = "http://xml.weather.yahoo.com/forecastrss?p="
            self.full_url = ''
            self.__code = ''
            self.__wdo = ''

    def send_req(self):
            self.full_url = self.url + self.__code
            req = urllib2.Request(self.full_url)
            opener = urllib2.build_opener()
            #this is going to get the information for us
            data = opener.open(req)
            #parse it
            xmldoc = minidom.parse(data)
            #find the tags we want and put that info into the wdo
            self.__wdo = WeatherDataObject() #instance of the data object class
            condition = xmldoc.getElementsByTagName('yweather:condition')
            self.__wdo.temp = condition[0].attributes['text'].value
            self.__wdo.code = condition[0].attributes['code'].value
            location = xmldoc.getElementsByTagName('yweather:location')
            self.__wdo.location = location[0].attributes['city'].value

    #dont want anyone overwriting my data object so I am making a property with just a getter
    @property
    def wdo(self):
        return self.__wdo


#nodes:
    #nested tags: use firstChild
    #if it is a stand alone element, we need to access it by using whatever the
    #tag name is + [0], meaning we access the first element of the array,
    #although there is only one element i.e. condition[0] - we are accessing
    #the first element (called text, see below) of the tag yweather:condition.
    # This is the xml tag:<yweather:condition text="Fair" code="34" temp="84" date="Wed, 21 May 2014 6:51 pm EDT"/>
    #we accessed yweather:condition and then drilled into "text"
# <tag>
    #<X>
        #<Y>
#

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, new_code):
        self.__code = new_code

class WeatherDataObject(object):
    '''this holds the information sent by the API'''
    def __init__(self):
        self.location = ''
        self.temp = ''
        self.condition = ''
        self.code = 0 #this "code" is the weather code, not the zip code