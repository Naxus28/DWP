# Gabriel Ferraz
# 05/14/2014
# simple form
import webapp2
from page import MyClass
class MainHandler(webapp2.RequestHandler):
    def get(self):
        from datetime import date
        if self.request.GET:
            name1 = self.request.GET["firstName"]
            name2 = self.request.GET["lastName"]
            keyword = self.request.GET["keyWord"]
            gender = self.request.GET["gender"]
            reason = self.request.GET["select"]
            picture = self.request.GET["picture"]
            date = date.today()

            if not picture:
                if gender == "Male":
                    picture = "images/cartman.png"
                else:
                    picture = "images/marjorine.png"

            if "checkbox" in self.request.GET:
                checkbox = True
            else:
                checkbox = False

            view = MyClass(name1, name2, keyword, gender, reason, picture, date)
            if name1 and name2 and keyword and gender and reason and checkbox and picture:
                self.response.write(view.page2())
            else:
                view = MyClass()
                self.response.write(view.error())
        else:
            view = MyClass()
            self.response.write(view.main())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
