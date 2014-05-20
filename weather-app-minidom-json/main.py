import webapp2
from page import Page
from page import FormPage

#libraries for working with xml in python
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.form_header = "Open Weather Map API"

        #if there are URL variables...
        if self.request.GET:
            code = self.request.GET['code']
        #go get the api info
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + code
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            #this is going to get the information for us
            data = opener.open(req)
        #parse it
            jsondoc = json.load(data)
            content = jsondoc['main']['temp']
            view.page_content = "</br>This is the temperature in Kelvins: " + str(content)
            fahrenheit = 1.8*(content-273)
            view.page_content += "</br> Temperature in Fahrenheit: " + str(fahrenheit)
            view.page_content += "</br> Temperature in Celcius: " + str((fahrenheit-32)*5/9)

            #print jsondoc['coord']


            self.response.write(content)



        #print out
        self.response.write(view.print_out())
                #print "found"


        #look at elements within it

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
