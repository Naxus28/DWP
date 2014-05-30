import webapp2
from page import Page
from page import FormPage

#libraries for working with xml in python
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()

        #if there are URL variables...
        if self.request.GET:
            code = self.request.GET['code']
        #go get the api info
            url = "http://xml.weather.yahoo.com/forecastrss?p=" + code
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            #this is going to get the information for us
            data = opener.open(req)
        #parse it
            xmldoc = minidom.parse(data)
            #self.response.write(content)
            list = xmldoc.getElementsByTagName('yweather:forecast')
            content = xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue + "</br>"
            print content

            for item in list:
                content += item.attributes['day'].value + ": "
                content += "High of " + item.attributes['high'].value
                content += " | Low of " + item.attributes['low'].value
                content += " | Condition " + item.attributes['text'].value
                content += "<img width='60' src = 'images/'" + item.attributes['code'].value + ".png />"
                content += "</br>"

                print item
            #self.response.write(content)
            view.page_content = content
        #print out
        self.response.write(view.print_out())
                #print "found"


        #look at elements within it

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
