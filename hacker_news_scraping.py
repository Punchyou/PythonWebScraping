from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re
from pprint import pprint
import inspect
from collections import OrderedDict
import json

def simple_get(url):
    """Attempts to get the content at 'url' by making an HTTP GET request."""

    try:
        with closing(get(url, stream = True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """Returns True if the response seems to be HTML, False otherwise."""
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def log_error(e):
    print(e)

def store_all_data():
    """Downloads the page where expected data are found and returns a list of strings."""

    input_number = 20
    url = "https://news.ycombinator.com/"
    response = simple_get(url)
    html = BeautifulSoup(response, 'html.parser')
    
    if response is not None:
        html, point, author, comment, rank = find_data(response, html)
        HN_list = make_list_of_HNdata_dictionaries(input_number, html, point, author, comment, rank)
        return HN_list

    # Raise an exception if we failed to get any data from the url.
    raise Exception('Error retreiving contents at {}'.format(url))

def find_data(response, html):
    """ Finds points, author names, comments and ranks from html."""
    point = html.find_all('span', attrs={'class': re.compile("^scor")})
    author = html.find_all('a', attrs={'href': re.compile("^user")})
    comment = html.find_all('a', text= re.compile("comment|comments|discuss"))
    rank = html.find_all('span', attrs={'class': re.compile("^rank")})

    return html, point, author, comment, rank

def make_list_of_HNdata_dictionaries(input_number, html, points, authors, comments, ranks):
    """ Makes a list of all the data that retrieves from the html."""
    hacker_news_list = []
    for pos_a, a in enumerate(html.find_all('a', attrs={'href': re.compile("^htt")}, limit= input_number + 1)[1:]):
            hacker_dict =  OrderedDict()
            hacker_dict["title"] = a.text
            hacker_dict["uri"] = a.get('href').strip().encode("utf-8").decode("utf-8")
            hacker_dict["author"] = authors[pos_a].text
            hacker_dict["points"] = int(points[pos_a].text[:-7])
            hacker_dict["comments"] = (
            0 if comments[pos_a+1].text[-7:] == "discuss"
            else int(comments[pos_a+1].text.encode("ascii", "ignore")[:-7].decode("utf-8")) if comments[pos_a+1].text[-7:] == "comment"
            else int(comments[pos_a+1].text.encode("ascii", "ignore")[:-8].decode("utf-8"))
            )
            hacker_dict["rank"] = int(ranks[pos_a].text[:-1])
            hacker_news_list.append(hacker_dict)
    return hacker_news_list



def print_engine(store_all_data):
    """ Creates the desired output format."""
    for d in store_all_data():
        print(json.dumps(d, indent=1) + "," if d != store_all_data()[-1] else json.dumps(d, indent=1))

def add(x,y):
    """ For unit testing purposes only."""
    return x + y

print_engine(store_all_data)