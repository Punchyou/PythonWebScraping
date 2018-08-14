import re

class FindHNData():

    def __init__(self):
        self.points = "points"
        self.author = "author"
        self.comments = "comments"
        self.rank = "rank"
    

    def find_data(self, response, html):
        """ Finds points, author names, comments and ranks from html."""
        self.point = html.find_all('span', attrs={'class': re.compile("^scor")})
        self.author = html.find_all('a', attrs={'href': re.compile("^user")})
        self.comment = html.find_all('a', text= re.compile("^comment|comments|discuss"))
        self.rank = html.find_all('span', attrs={'class': re.compile("^rank")})
        return FindHNData