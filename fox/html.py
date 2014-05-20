# This class handles the html template. It works as a super class and has to be
#passed into each one of the animals subclasses just like the Animal class itself.

class Html(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.main_title} | {self.title}</title>
        <link rel="stylesheet" type="text/css" href={self.css}>
        <link href={self._font} rel="stylesheet" type="text/css">
        <script src="js/modernizr.2.5.3.min.js"></script>

    </head>
    <header>
        <h1>The Animals Page</h1>
        <nav>
            <ul>
                <li><a href="?animal=rabbit">THE RABBIT</a></li>
                <li><a href="?animal=wolf">THE WOLF</a></li>
                <li><a href="?animal=fox">THE FOX</a></li>
            </ul>
        </nav>
    </header>
    <body id="{self._body_id}">
        '''
        self._content = '''
        </div>
        <div id="info">
            <h2>Information about the {self.animal}</h2>
            <p><span>Phylum:</span> {self._phylum}</p>
            <p><span>Class:</span> {self._class_}</p>
            <p><span>Order:</span> {self._order}</p>
            <p><span>Family:</span> {self._family}</p>
            <p><span>Genus:</span> {self._genus}</p>
            <p><span>Average Life Span:</span> {self._avg_lifespan}</p>
            <p><span>Habitat:</span> {self._habitat}</p>
            <p><span>Geo Location:</span> {self._geo_location}</p>
            <p><span>Typical sound emitted:</span> {self.sound}</p>
        </div>
        <div id ="image">
            <h2 id="animal_image">This is the {self.animal}</h2>
            <figure>
                <img id ="the_fox" src="{self._fox}" alt="">
                <img id ="the_image" src="{self._url}" alt="{self.animal}">
                <figcaption>Original image can be found at <a href ="{self._url}" target="_blank">{self._link}</a></figcaption>
            </figure>
            <p id="my_bad">OOPS...MY BAD!<span>(or maybe not ;)</span></p>
        </div>
        '''

        self._close = '''
        <script src="js/jquery-1.11.0.min.js"></script>
        <script src="js/init.js"></script>
    </body>
</html>
        '''
