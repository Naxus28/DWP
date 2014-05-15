class Phone(object):
    def __init__(self):
        self.__phone = ""
        self.__price = 0
        self.__case = 0
        self.__film = 0
        self.__warranty = 0
        self.__tax = 0
        self.__total = 0
        self.__open = '''

<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
        <link href='http://fonts.googleapis.com/css?family=Lato|Raleway' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Nobile' rel='stylesheet' type='text/css'>
        <title>The Phone Page</title>
    </head>
    <body>
        '''
        self.header = '''
        <header>
            <h1>THE PHONE PAGE</h1>
        </header>
        '''
        self.__paragraphs = '''
        <div id="links">
            <h2 id="firstH2">PHONE MODELS</h2>
            <a href="?phone=iphone">iPhone 5s</a>
            <a href="?phone=galaxy">Galaxy</a>
            <a href="?phone=lg">LG</a>
            <a href="?phone=nexus">Nexus 7</a>
            <a href="?phone=windows">Windows Phone</a>
       </div>
       <div id="paragraphs">
            <h2>PHONE INFO</h2>
            <p id = brand>You are checking out the {self.phone}</p>
            <p id="package">This is the cost of the full package:</p>
            <p id = price>Phone: ${self.price}</p>
            <p id = case>Case: ${self.case}</p>
            <p id = film>Film: ${self.film}</p>
            <p id = warranty>Warranty: ${self.warranty}</p>
            <p id = tax>Tax: ${self.tax}</p>
            <p id = total>Total: ${self.total}</p>
        </div>
        '''
        self.__close = '''
    </body>
</html>
        '''
        self.__all = self.__open + self.header + self.__paragraphs + self.__close

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @property
    def film(self):
        return self.__film

    @film.setter
    def film(self, new_film):
        self.__film = new_film

    @property
    def case(self):
        return self.__case

    @case.setter
    def case(self, new_case):
        self.__case = new_case

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, new_total):
        if new_total < 800:
            self.__total = str(new_total) + " THIS IS A PROMOTION!"
        else:
            self.__total = new_total


    # def printer(self):
    #     print self.__case

    def print_out(self):
        self.update()
        return self.__all

    def update(self):
        self.__all = self.__all.format(**locals())

