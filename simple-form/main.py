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

import webapp2
#from FILE import CLASSNAME
from page import HTMLPage

#blueprint for creating the web app
class MainHandler(webapp2.RequestHandler):
    #catalist - start our web app
    #when the app loads this function gets called

    def get(self):
        #prints out to the browser
         #p is the instance (object) and HTMLPage is the object used to creat it
        #instance.attribute
        #instance.method()


        #self.response.write(p.page_open + p.page_content + p.page_close)


    #or we could also call the function print_out and have the same result
        if self.request.GET:
            fn = self.request.GET["firstname"]
            ln = self.request.GET["lastname"]
            p = HTMLPage(fn, ln)
            if fn and ln:
                print "these are fn and ln: " + fn + " " + ln
                self.response.write(p.call_variables())
            else:
                print "these are fn and ln: " + fn + " " + ln
                self.response.write(p.error())
        else:
            p = HTMLPage("", "")
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
