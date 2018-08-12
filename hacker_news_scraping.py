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
        print("You value is correct")
        return num_Of_URLs
    else:
        print("Please enter a positive integer, in the range of 1 to 100.")
        get_user_input()


def store_all_data(user_input):
    """Downloads the page where expected data are found and returns a list of strings."""
    url = "https://news.ycombinator.com/"
    response = simple_get(url)
    html = BeautifulSoup(response, 'html.parser')
    if response is not None:
        html, point, author, comment, rank = find_data(response, html)
        HN_list = make_list_of_HNdata_dictionaries(user_input, html, point, author, comment, rank)
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
        rec_titles = a.text
        rec_URIs = a.get('href').strip().encode("utf-8").decode("utf-8")
        rec_authors = authors[pos_a].text
        rec_points = int(points[pos_a].text[:-7])
        rec_comments = (
        0 if comments[pos_a+1].text[-7:] == "discuss"
        else int(comments[pos_a+1].text.encode("ascii", "ignore")[:-7].decode("utf-8")) if comments[pos_a+1].text[-7:] == "comment"
        else int(comments[pos_a+1].text.encode("ascii", "ignore")[:-8].decode("utf-8"))
        )
        rec_ranks = int(ranks[pos_a].text[:-1])
        if not validate_fetched_record(rec_titles, rec_authors, rec_URIs, rec_points, rec_comments, rec_ranks):
            continue
        hacker_dict =  OrderedDict()
        hacker_dict["title"] = rec_titles
        hacker_dict["uri"] = rec_URIs
        hacker_dict["author"] = rec_authors
        hacker_dict["points"] = rec_points
        hacker_dict["comments"] = rec_comments
        hacker_dict["rank"] = rec_ranks
        hacker_news_list.append(hacker_dict)
    return hacker_news_list

def validate_fetched_record(rec_titles, rec_authors, rec_URIs, rec_points, rec_comments, rec_ranks):
    if len(rec_titles) > 256:
        return False
    if len(rec_authors) > 256: 
        return False
    if not isinstance(rec_points, int) or rec_points < 0:
        return False
    if not isinstance(rec_comments, int) or rec_comments < 0:
        return False
    if not isinstance(rec_ranks, int) or rec_ranks < 0:
        return False
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not re.match(regex, rec_URIs):
        return False
    return True

def print_engine(store_all_data, an_input):
    """ Creates the desired output format."""
    for d in store_all_data(an_input):
        print(json.dumps(d, indent=1) + "," if d != store_all_data(an_input)[-1] else json.dumps(d, indent=1))

def add(x,y):
    """ For unit testing purposes only."""
    return x + y

an_input = get_user_input()
print_engine(store_all_data, an_input)