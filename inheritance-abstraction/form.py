from page import Page

class FormPage(Page):
    def __init__(self):
        #call constructor function
        Page.__init__(self)
        self.__form_open = '<form method=GET action="">'
        self.__inputs = '''
        <input type = 'text' name='firstName' placeholder='First Name'>
        <input type = 'text' name='lastName' placeholder='Last Name'>
        <input type = 'submit' name='firstName'>
        '''
        self.__form_close = '</form>'
        self.form_header =">>Form Header<<"
        self._content = self.form_header + self.__form_open + self.__inputs + self.__form_close

    def update(self):
        self.all = self._open + self.form_header + self.__form_open + self.__inputs + self.__form_close + self._close
        self.all = self.all.format(**locals())

        print self._content


