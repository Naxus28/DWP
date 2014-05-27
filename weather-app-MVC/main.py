import webapp2
from page import Page
from page import FormPage
from model import WeatherDataObject

#libraries for working with xml in python

from model import WeatherModel


class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        #if there are URL variables...
        if self.request.GET:
            w_model = WeatherModel()
            w_model.code = self.request.GET['code']
            w_model.send_req() #connect to API
            w_view = WeatherView()#the view that is going to sshow my info
            w_view.wdo = w_model.wdo # transfer wdo from model to view
            w_view.update_view()
            view.page_content = w_view.content #creates html using our wdo

        self.response.write(view.print_out())

                #print "found"
class WeatherView(object):
    '''This class is showing JUST the weather information from the API '''
    def __init__(self):
        self.wdo = WeatherDataObject()
        self.content = ''
    def update_view(self):
        self.content = '''
        <div>
            <h3>{self.wdo.location}</h3>
                <ul>
                    <li><strong>Temperature: </strong> {self.wdo.temp}</li>
                    <li><strong> City: </strong> {self.wdo.location} </li>
                </ul>
        </div>
        '''
        self.content = self.content.format(**locals())
        #print self.content

        #look at elements within it

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
