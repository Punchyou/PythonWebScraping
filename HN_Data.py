import hacker_news_scraping as hns

class HNData():

    def __init__(self, title, author, points, comments, rank):
        self.title = title
        self.author = author
        self.points = points
        self.comments = comments
        self.rank = rank

