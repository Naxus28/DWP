class MyClass(object):
    def __init__(self):
        self.page_open='''
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
        self.paragraph1 = '''
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
                <input class="radio" type="radio" name="genre" id="female" value="Female" /> <label class="radio" for="female">Female</label>
                <input class="radio" type="radio" name="genre" id="male" value="Male" /> <label class="radio" for="female">Male</label>
                <select  name="select">
                     <option>I'm here to...</option>
                     <option value="learn">learn more about soccer</option>
                     <option value="find">find people to play with</option>
                     <option value="read">read the news about soccer</option>
                     <option value="message">exchange messages with soccer fans</option>
                </select>
               <p id="check"> <input type="checkbox" name="checkbox" class="checkbox" id="checkB"><label for="checkbox" class="checkbox">
               I agree with the <a>terms of use</z></label></p>
               <input id="submit" type="submit" name="submit" value="Sign up"/>
            </form>
        </div>
        '''
        self.background_div = '''
        <div id="background"></div>
        '''
        self.close_page = '''
    </body>

</html>
'''
    def main(self):
        return self.page_open + self.header + self.paragraph1 + self.background_div + self.close_page