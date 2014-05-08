class HTMLPage(object):
    def __init__(self, var1, var2):
        global name
        name = "name"
        self.page_open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to my Page</title>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
    </head>
    <body>
        '''
        self.page_content = '''
        <form method="GET" action="">
            <input type="text" name="firstname" placeholder="firstname"/>
            <input type="text" name="lastname" placeholder="lastname"/>
            <input type="submit" name="submit" value="go"/>
        </form>
        '''
        self.open_paragraph = '''
        <p id="name">
        '''
        self.names = var1 + " " + var2
        self.close_paragraph = '''
        <a href="http://localhost:8080"> < Back to Form<a>
        </p>
        '''
        self.paragraph1 = '''
        <p id="error"> We are sorry but something went wrong. Please include all information and try again.
        </p>
        <a href="http://localhost:8080"> < Back to Form<a>
        '''
        self.page_close = '''
    </body>
</html>
        '''
    def print_out(self):
        #print name
        return self.page_open + self.page_content + self.page_close

    def call_variables(self):
        return self.page_open + self.open_paragraph + self.names + self.close_paragraph + self.page_close

    def error(self):
        return self.page_open + self.paragraph1 + self.page_close