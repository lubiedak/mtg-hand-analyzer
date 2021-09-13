import cherrypy


class Page:
    # Store the page title in a class attribute
    title = 'Untitled Page'

    def header(self):
        return '''
            <html>
            <head>
                <title>%s</title>
            <head>
            <body>
            <h2>%s</h2>
        ''' % (self.title, self.title)


    def footer(self):
        return '''
            </body>
            </html>
        '''



class HomePage(Page):
    # Different title for this page
    title = 'Tutorial 5'

    def __init__(self):
        # create a subpage
        self.another = AnotherPage()

    @cherrypy.expose
    def index(self):
        # Note that we call the header and footer methods inherited
        # from the Page class!
        return self.header() + '''
            <p>
            Isn't this exciting? There's
            <a href="./another/">another page</a>, too!
            </p>
        ''' + self.footer()



class AnotherPage(Page):
    title = 'Another Page'

    @cherrypy.expose
    def index(self):
        return self.header() + '''
            <p>
            And this is the amazing second page!
            </p>
        ''' + self.footer()


if __name__ == "__main__":
    cherrypy.quickstart(HomePage())
