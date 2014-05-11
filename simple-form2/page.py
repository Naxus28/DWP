class MyClass(object):
    def __init__(self, name1=" ", name2=" ", key=" ", gender=" ", reason=" ", picture=" "):
        self.page_open = '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
        <link href='http://fonts.googleapis.com/css?family=Lato|Raleway' rel='stylesheet' type='text/css'>
        <title>The Soccer Network</title>
    </head>
    <body>
    '''
        self.header = '''
        <header>
            <h1>The Soccer Network</h1>
        </header>
        '''
        #=====first page content=============
        #left div, right div (form), and background picture
        self.content = '''
        <div class="container" id="left_container">
            <h2>WHAT YOU GET</h2>
            <ul>
                <li>Be part of the largest soccer network on the planet</li>
                <li>Find people who share the same passion for soccer as you</li>
                <li>Participate in soccer events with new friends</li>
                <li>Keep informed about the latest soccer news</li>
                <li>Have fun!</li>
            </ul>
        </div>
        <div class="container" id="right_container">
            <h2>SIGN UP</h2>
            <form method="GET" action="">
                <input class="name" type="text" name="firstName" placeholder="First Name">
                <input class="name" type="text" name="lastName" placeholder="Last Name">
                <input class="password" type="password" name="keyWord" placeholder="Password">
                <input class="picture" type="text" name="picture" placeholder="Picture URL i.e. http://www.my_picture.com">
                <p id="radio_par">
                    <input class="radio" type="radio" name="gender" id="female" value="Female" checked="checked"/> <label class="radio" for="female">Female</label>
                    <input class="radio" type="radio" name="gender" id="male" value="Male" /> <label class="radio" for="female">Male</label>
                </p>
                <select  name="select">
                     <option>I'm here to...</option>
                     <option value="learn more about soccer">learn more about soccer</option>
                     <option value="find people to play with">find people to play with</option>
                     <option value="read news about soccer">read news about soccer</option>
                     <option value="exchange messages with soccer fans">exchange messages with soccer fans</option>
                     <option value="have fun!">have fun!</option>
                </select>
               <p id="check"> <input type="checkbox" value="true" name="checkbox" checked="checked" class="checkbox" id="checkB">
               <label for="checkbox" class="checkbox">
               I agree with the <a href="#">terms of use</a></label></p>
               <input id="submit" type="submit" name="submit" value="Sign up"/>
            </form>
        </div>
        '''
        #this div is used for the background picture; it allows me
        #to change the opacity of the bg picture without changing the opacity
        #of the text--which would happen if I placed the pic on the body
        self.background_div = '''
        <div id="background"></div>
        '''

        #========second page content===========
        self.open_container2 = '''
        <div id="profile">
        '''
        self.open_h2 = '''
            <h2 id="nameParagraph">
            Welcome to The Soccer Network,
        '''
        self.name_h2 = " " + name1 + " " + name2

        self.close_h2 = '''
            </h2>
        '''
        self.open_picture = '''

            <img value = "image" src="
        '''
        self.picture = picture

        self.close_picture = '''
            " />
        '''

        self.paragraph1 = '''
            <p>
            Here is your account information:
            </p>
        '''
        self.open_password_paragraph = '''
         <p id="passwordParagraph">
        '''
        self.password_paragraph = "Password: " + key

        self.close_password_paragraph = '''
            </p>
        '''

        self.open_gender = '''
            <p id="gender">
        '''
        self.gender = "Gender: " + gender

        self.close_gender = '''
            </p>
        '''

        self.open_reason = '''
            <p id="gender">
        '''
        self.reason = "The reason you signed up:" + reason

        self.close_reason = '''
            </p>
        '''

        self.close_container2 = '''
        </div>
        '''
        self.background_div2 = '''
        <div id="background2"></div>
        '''
        self.close_page = '''
    </body>

</html>
'''
    def main(self):
        return self.page_open + self.header + self.content + self.background_div + self.close_page

    def page2(self):
        return self.page_open + self.header + self.open_container2 + self.open_h2 + self.name_h2 + \
               self.close_h2 + self.open_picture + self.picture + self.close_picture + self.paragraph1+ \
               self.open_password_paragraph + self.password_paragraph +\
               self.close_password_paragraph + self.open_gender + self.gender + self.close_gender + self.open_reason + \
               self.reason + self.close_reason + self.close_container2 + self.background_div2 + self.close_page