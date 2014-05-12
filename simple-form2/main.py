#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
