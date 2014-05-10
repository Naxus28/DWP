class MyClass(object):
    def __init__(self):
        self.page_open='''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
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
            <p>Be part of the largest soccer network on the planet</p>
            <p>Find people who share the same passion for soccer as you</p>
            <p>Participate in soccer in events with new friends</p>
            <p>Keep informed about the latest soccer news</p>
        </div>
        <div class="container" id="right_container">
            <h2>SIGN UP</h2>
            <form>
                <input class="name" type="text" name="firstName" placeholder="First Name">
                <input class="name" type="text" name="lastName" placeholder="Last Name">
                <input class="radio" type="radio" name="genre" id="female" value="Female" /> <label for="female">Female</label>
                <input class="radio" type="radio" name="genre" id="male" value="Male" /> <label for="female">Male</label>
                <p></p>
                <label for="Select">Choose your level of passion</label>
                <select name="select">
                     <option value="volvo">Volvo</option>
                     <option value="saab">Saab</option>
                     <option value="mercedes">Mercedes</option>
                     <option value="audi">Audi</option>
                </select>
                <input type="checkbox" name="checkbox" class="checkbox" id="checkB"><label for="checkbox" class="checkbox">I agree with the <a>terms of use</z></label>
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