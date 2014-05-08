class HTMLPage(object):
    def __init__(self):
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
        self.page_close = '''
    </body>
</html>
        '''
    def print_out(self, content=""):
        print name
        return self.page_open + self.page_content + content + self.page_close

    def call_variables(self,var1,var2):
        self.open_paragraph ='''
        <p>
        '''
        self.names = var1 +" "+ var2

        self.close_paragraph = '''
        </p>
        '''
        return self.open_paragraph + self.names + self.close_paragraph


