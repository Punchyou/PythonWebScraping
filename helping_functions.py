from collections import OrderedDict
import re
from HN_Data import HNData

def get_user_input():
    """ Gets the number of urls from user and promts the user again if its not valid."""
    while True:
        try:
            num_Of_URLs = int(input("Enter the number of URLs to be fetched: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            break
    if num_Of_URLs > 0 and num_Of_URLs <= 100: 
        return num_Of_URLs
    else:
        print("Please enter a positive integer, in the range of 1 to 100.")


def make_list_of_HNdata(input_number, html, points, authors, comments, ranks):
    """ Makes a list of all the data that retrieves from the html."""
    hacker_news_list = []
    for pos_a, a in enumerate(html.find_all('a', attrs={'href': re.compile("^htt")}, limit= input_number + 1)[1:]):
        hn_data = HNData(a.text, authors[pos_a].text, a.get('href').strip().encode("utf-8").decode("utf-8"), int(points[pos_a].text[:-7]), (
        0 if comments[pos_a+1].text[-7:] == "discuss"
        else int(comments[pos_a+1].text.encode("ascii", "ignore")[:-7].decode("utf-8")) if comments[pos_a+1].text[-7:] == "comment"
        else int(comments[pos_a+1].text.encode("ascii", "ignore")[:-8].decode("utf-8"))
        ), int(ranks[pos_a].text[:-1]))
        if not validate_fetched_record(hn_data):
            continue
        hacker_news_list.append(hn_data.__dict__)
    return hacker_news_list

def validate_fetched_record(hn_data):
    if not hn_data.title or not isinstance(hn_data.title, str) or len(hn_data.title) > 256:
        return False
    if not hn_data.author or not isinstance(hn_data.author, str) or len(hn_data.author) > 256: 
        return False
    if not isinstance(hn_data.points, int) or hn_data.points < 0:
        return False
    if not isinstance(hn_data.comments, int) or hn_data.comments < 0:
        return False
    if not isinstance(hn_data.rank, int) or hn_data.rank < 0:
        return False
    validate_uri_record(hn_data)
    return True

def validate_uri_record(hn_data):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not re.match(regex, hn_data.uri):
        return False