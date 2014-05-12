class MyClass(object):
    def __init__(self, name1=" ", name2=" ", key=" ", gender=" ", reason=" ", picture=" ", date=" "):
        self.page_open = '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
        <link href='http://fonts.googleapis.com/css?family=Lato|Raleway' rel='stylesheet' type='text/css'>
        <title>The Soccer Network</title>
    </head>
    '''
        self.body1 = '''
    <body id="body1">
    '''
        self.body2 = '''
    <body id="body2">
    '''
        self.header_open = '''
        <header>
            <h1>The Soccer Network</h1>
        '''
        self.logout = '''
         <a href="http://localhost:9080">LOG OUT</a>
        '''
        self.header_close = '''
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
                <input class="picture" type="text" name="picture" placeholder="Picture URL (i.e. http://www.my_picture.com/picture.jpg)">
                <p id="radio_par">
                    <input class="radio" type="radio" name="gender" id="male" value="Male" checked="checked" /> <label class="radio" for="male">Male</label>
                    <input class="radio" type="radio" name="gender" id="female" value="Female" /> <label class="radio" for="female">Female</label>
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

        self.content2 = '''
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
            <img id="ball" src="images/funny_ball.png" />
            <h2 id="h2_error">An error occurred. Please fill out all form fields (you may leave the picture field empty).</h2>
            <a href="http://localhost:9080">Back to Form</a>
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
            <h2 id="welcomeMsg">
            Welcome to The Soccer Network,
        '''
        self.name_h2 = " " + name1 + " " + name2 + "!"

        self.close_h2 = '''
            </h2>
        '''
        self.open_picture = '''
            <img src="
        '''
        self.picture = picture

        self.close_picture = '''
            " />
        '''

        self.paragraph1 = '''
            <p class="profile_paragraphs" id="header">
            Here is your account information:
            </p>
        '''
        self.open_password_paragraph = '''
         <p class="profile_paragraphs">
        '''
        self.password_paragraph = "Password: " + key

        self.close_password_paragraph = '''
            </p>
        '''

        self.open_gender = '''
            <p class="profile_paragraphs">
        '''
        self.gender = "Gender: " + gender

        self.close_gender = '''
            </p>
        '''

        self.open_reason = '''
            <p class="profile_paragraphs">
        '''
        self.reason = "You are here to " + reason

        self.open_date = '''
        <p class="profile_paragraphs">
        '''
        self.date = "You are a member since " + str(date)
        self.close_date = '''
        </p>
        '''
        self.close_reason = '''
            </p>
        '''
        self.close_container2 = '''
        </div>
        '''
        self.close_wrapper = '''
        <div id="wrapper">
        '''
        self.close_body1 = '''
    </body>
    '''
        self.close_body2 = '''
    </body>
    '''

        self.close_page = '''
</html>
'''
    def main(self):
        return self.page_open + self.body1 + self.header_open + self.header_close + self.content + self.background_div + self.close_body1 + self.close_page

    def page2(self):
        return self.page_open + self.body2 + self.header_open + self.logout + self.header_close + self.open_container2 + self.open_h2 + self.name_h2 + \
               self.close_h2 + self.open_picture + self.picture + self.close_picture + self.paragraph1+ \
               self.open_password_paragraph + self.password_paragraph +\
               self.close_password_paragraph + self.open_gender + self.gender + self.close_gender + self.open_reason + \
               self.reason + self.close_reason + self.open_date + self.date + self.close_date + self.close_container2 + self.close_body2 + self.close_page

    def error(self):
        return self.page_open + self.body1 + self.header_open + self.header_close + self.content2 + self.background_div + self.close_body1+ self.close_page

