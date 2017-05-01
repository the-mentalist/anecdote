class Movie():
    """ Consists of information related to Movie
		Args:
			title: Title of Movie
			img: url of poster
			trailer_url: url of trailer
			storyline: Movie storyline
    """
    def __init__(self, title, img, trailer_url, storyline):
        # Constructor
        self.title=title
        self.img=img
        self.trailer_url=trailer_url
        self.storyline=storyline
    def getTrailerUrl(self):
        return self.trailer_url
    def getStoryline(self):
        return self.storyline
    def getTitle(self):
        return self.title
    def getImg(self):
        return self.img
