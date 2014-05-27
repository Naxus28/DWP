from model import FlickrDataObject
from model import FlickrDataObject2

class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="css/styles.css">
        <link href='http://fonts.googleapis.com/css?family=Lustria|Marcellus+SC|Brawler|Fontdiner+Swanky|Handlee|Libre+Baskerville|Architects+Daughter|Forum' rel='stylesheet' type='text/css'>
    </head>
    <body>
        '''
        self.header = "<h1>The Picture Mosaic</h1>"
        self._content = "<h1>This is the content</h1>"
        self._close = '''
        <script src="js/jquery-1.11.0.min.js"></script>
        <script src="js/jquery-ui-1.10.4.custom.min.js"></script>
        <script src="js/init.js"></script>
    </body>
</html>
        '''
        self.open_pictures_container = ""
        self.close_pictures_container = ""
        self.searched_pictures = ""
        self.page_content = ""
        self.alert_msg = ""
        self._title = "The Picture Mosaic | Powered by Flickr"
        #self.all = self._open + self.header + self._content + self._close

    @property
    def title(self):
        return self._title

    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self, c):
            self._css_url = c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self.open_pictures_container + self.close_pictures_container + self._close
        self.all = self.all.format(**locals())


class FormPage(Page):
    def __init__(self):
        #call constructor function
        Page.__init__(self)

        self.__form_open = '<form method=GET action="">'
        self.__inputs = '''
            <input id = "textfield" type = 'text' name='query' placeholder='Search Picture'>
            <input id = "button" type = 'submit' value="SEARCH">
        '''
        self.__form_close = '</form>'
        self.open_pictures_container = "<div id = 'results_wrapper'>"
        self.close_pictures_container = "</div>"
        self.alert_msg = "<p id='alert'>Click and drag to build your mosaic or click for full view</p>"
        self._content = self.__form_open + self.__inputs + self.__form_close
        self.all = ""
        self.search_results_header = ""
        self._arrow = "<img id = 'arrow' src = 'images/arrow1.png'/>"
        self.searched_pictures = ""

    def update(self):
        self.all = self._open + self.header + self.alert_msg + self._content + \
            self.page_content + self.open_pictures_container + self.search_results_header + self.searched_pictures + \
            self._arrow + self.close_pictures_container + self._close
        self.all = self.all.format(**locals())

    @property
    def search_header_update(self):
        return self.search_results_header

    @search_header_update.setter
    def search_header_update(self, new_header):
        self.search_results_header = new_header

    @property
    def arrow_up(self):
        return self._arrow

    @arrow_up.setter
    def arrow_up(self, new_arrow):
        self._arrow = new_arrow


#object that shows the flickr.getRecent API data
class FlickrView(object):
    def __init__(self):
        self.api_view = FlickrDataObject()
        self.api_content = ""

    def update_api_view(self):
        for url in range(0, 50):
            #push the pictures to the view
            self.api_content += '''
            <div class='img-container'>
                <a href={self.api_view.the_urls['''+str(url)+''']} target='_blank'><img src = {self.api_view.the_urls['''+str(url)+''']}></a>
            </div>
        '''
        self.api_content = self.api_content.format(**locals())
        #print self.api_content

#object that shows the flickr.photo.Search API data
class FlickrView2(object):
    def __init__(self):
        self.api_view2 = FlickrDataObject2()
        self.api_header2 = ""
        self.api_content2 = ""
        self.full_content = ""
        print self.api_view2.query

    def update_api_view2(self):
        # self.api_header2 = '''
        #     <h2>Search Result:{self.api_view2.picture_array_length} pictures  <span id='more_pics'>(for more pictures on this topic, visit <a href= 'https://www.flickr.com/search/
        #                                      ?q={self.api_view2.query}' target = '_blank'>Flickr.com</a>)</span></h2>'''
        for search_url in range(0, 100):

            #create the h2 and push the pictures to the view
            self.api_content2 += '''
             <div class='picture_container'>
                 <div class='new_pictures'>
                      <a href={self.api_view2.the_search_urls['''+str(search_url)+''']}
                      target='_blank'><img src ={self.api_view2.the_search_urls['''+str(search_url)+''']}></a>"
                  </div>
                  <div id='users'>
                     <a href={self.api_view2.users_urls['''+str(search_url)+''']} target='_blank'>Photographer's Flickr Profile</a>
                 </div>
              </div>
          '''
        self.api_content2 = self.api_content2.format(**locals())
        #self.full_content = self.api_header2 + self.api_content2









