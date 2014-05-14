import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        yoda = Character()
        yoda.name = "Jedi Master Yoda"
        yoda.age = 900
        yoda.occupation = "Jedi Master"
        yoda.gender = "Male"
        yoda.print_info()
        print yoda.age
        #istance.attribute
        #instance.method()
        #instance.property

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.gender = "Male"
        luke.age = 19
        luke.occupation = "Jedi Knight"
        luke.print_info()
        print luke.age

        leia = Character()
        leia.name = "Leia Organa"
        leia.gender = "Female"
        leia.age = luke.age
        leia.occupation = "Princess"
        leia.squad_no = "pink5"
        print leia.squad_no
        print leia.age


class Character(object):
    def __init__(self):
        self.name = ""
        self.__age = 0
        self.occupation = ""
        self.gender = ""
        self.__rogue_squadron_no = "default"

    def print_info(self):
        print self.name + " is a(n) " + self.occupation

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age == 900:
            new_age = 1000
            self.__age = new_age
        elif new_age < 0 or new_age > 1000:
            print "error with age input!"
        else:
            self.__age = new_age

    @property
    def squad_no(self):
        return self.__rogue_squadron_no

    @squad_no.setter
    def squad_no(self, new_no):
        #validation
        if new_no == "pink5":
            new_no = "Red5"

        self.__rogue_squadron_no = new_no

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)






#
# import webapp2
#
# class MainHandler(webapp2.RequestHandler):
#
#     def get(self):
#         self.response.write('Hello world!')
#
#         yoda = Character()
#         yoda.name = "Yoda"
#         yoda.age = 900
#         yoda.gender = "Male"
#         yoda.occupation = "Jedi Master"
#         yoda.print_info()
#         yoda.squad_no = "Green 1"
#         print yoda.age
#         print yoda.squad_no
#
# #       yoda = Character()
# #       yoda.name = "Jedi Master Yoda"
# #       yoda.age = 900
# #       print yoda.age
#
#
#         luke = Character()
#         luke.name = "Luke"
#         luke.age = 24
#         luke.gender = "Male"
#         luke.occupation = "Jedi Knight"
#         luke.print_info()
#         luke.squad_no = "Red 4"
#         print luke.squad_no
#
#         leia = Character()
#         leia.name = "Leia"
#         leia.age = 24
#         leia.gender = "Female"
#         leia.occupation = "Princess"
#         leia.print_info()
#         leia.squad_no = "Pink 5"
#         print leia.squad_no
#
#
# class Character(object):
#     def __init__(self):
#                 self.name = ""
#                 self.__age = 0
#                 self.occupation = ""
#                 self.gender = ""
#                 self.__rogue_squadron_no = "DEFAULT"
#
#     def print_info(self):
#         print self.name + " is a(n) " + self.occupation
# #     def print_info(self):
# #         print self.name + " is a(n) " + self.occupation
#
#     @property
#     def age(self):
#         return self.__age
# #     @property
# #     def age(self):
# #         return self.__age
# #
#
#     @age.setter
#     def age(self, new_age):
#         if new_age == 900:
#             new_age = 1000
#             self.__age = new_age
#         else:
#             self.__age = new_age
#
#     #@age.setter
# #     def age(self, new_age):
# #         if new_age == 900:
# #             new_age = 1000
# #             self.__age = new_age
# #         else:
# #             self.__age = new_age
#
#     @property
#     def squad_no(self):
#         return self.__rogue_squadron_no
#
#     @squad_no.setter
#     def squad_no(self, new_no):
#
#         if new_no == "Pink 5":
#             new_no = "Red 1"
#
#         self.__rogue_squadron_no = new_no
#
# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)