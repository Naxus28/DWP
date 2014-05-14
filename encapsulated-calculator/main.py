# Gabriel Ferraz
# 05/14/2014
# Encapsulated Calculator


import webapp2
from page import Phone

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')

        #========first object========
        iphone = Phone()
        iphone.phone = "iPhone 5s"
        iphone.price = 500.00
        iphone.case = 30.00
        iphone.film = 20.00
        iphone.warranty = 230.00
        iphone.tax = 0.13
        iphone.printer()
        iphone.final_tax = (iphone.price + iphone.case + iphone.film + iphone.warranty) * iphone.tax
        iphone.total = iphone.price + iphone.case + iphone.film + iphone.warranty + iphone.final_tax

        #========second object========
        galaxy = Phone()
        galaxy.phone = "Galaxy 4"
        galaxy.price = 470.00
        galaxy.case = 35.00
        galaxy.film = 20.00
        galaxy.warranty = 210.00
        galaxy.tax = 0.13
        galaxy.final_tax = (galaxy.price + galaxy.case + galaxy.film + galaxy.warranty) * galaxy.tax
        galaxy.total = galaxy.price + galaxy.case + galaxy.film + galaxy.warranty + galaxy.final_tax

        #========third object========
        lg = Phone()
        lg.phone = "LG Flex"
        lg.price = 430.00
        lg.case = 25.00
        lg.film = 15.00
        lg.warranty = 180.00
        lg.tax = 0.13
        lg.final_tax = (lg.price + lg.case + lg.film + lg.warranty) * lg.tax
        lg.total = lg.price + lg.case + lg.film + lg.warranty + lg.final_tax

        #========fourth object========
        nexus = Phone()
        nexus.phone = "Nexus 7"
        nexus.price = 550.00
        nexus.case = 40.00
        nexus.film = 35.00
        nexus.warranty = 230.00
        nexus.tax = 0.13
        nexus.final_tax = (nexus.price + nexus.case + nexus.film + nexus.warranty) * nexus.tax
        nexus.total = nexus.price + nexus.case + nexus.film + nexus.warranty + nexus.final_tax

        #========fifth object========
        windows = Phone()
        windows.phone = "Windows Phone"
        windows.price = 575.00
        windows.case = 47.00
        windows.film = 32.00
        windows.warranty = 215.00
        windows.tax = 0.13
        windows.final_tax = (windows.price + windows.case + windows.film + windows.warranty) * windows.tax
        windows.total = windows.price + windows.case + windows.film + windows.warranty + windows.final_tax

        #==============defines which object will be displayed depending on
        #which link is clicked (links have the following href: <a href="?phone=phone_name_to_be_displayed">)
        # i.e. <a href="?phone=iphone">, <a href="?phone=galaxy">, etc
        if self.request.GET:
                the_phone = self.request.GET["phone"]
                if the_phone == "iphone":
                    self.response.write(iphone.print_out())
                elif the_phone == "galaxy":
                    self.response.write(galaxy.print_out())
                elif the_phone == "lg":
                    self.response.write(lg.print_out())
                elif the_phone == "nexus":
                    self.response.write(nexus.print_out())
                elif the_phone == "windows":
                    self.response.write(windows.print_out())
        else:
            self.response.write(iphone.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
