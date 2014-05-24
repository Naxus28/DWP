import soundcloud
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        # create a client object with your app credentials
        client = soundcloud.Client(client_id='a693cf81ad68e9357fe74bd43d212cf4')

        # get a tracks oembed data
        track_url = 'http://soundcloud.com/forss/flickermood'
        embed_info = client.get('/oembed', url=track_url)

        # print the html for the player widget
        print embed_info['html']

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
