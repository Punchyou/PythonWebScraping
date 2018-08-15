from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from re import compile
import json
from helping_functions import*
from HN_Data import HNData

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

def store_all_data(user_input, HNData):
    """Downloads the page where expected data are found and returns a list of strings."""
    url = "https://news.ycombinator.com/"
    response = simple_get(url)
    html = BeautifulSoup(response, 'html.parser')
    if response is not None:
        html, point, author, comment, rank = find_data(response, html)
        HN_list = make_list_of_HNdata(user_input, html, point, author, comment, rank)
        return HN_list

    # Raise an exception if we failed to get any data from the url.
    raise Exception('Error retreiving contents at {}'.format(url))

def find_data(response, html):
    """ Finds points, author names, comments and ranks from html."""
    point = html.find_all('span', attrs={'class': re.compile("^scor")})
    author = html.find_all('a', attrs={'href': re.compile("^user")})
    comment = html.find_all('a', text= re.compile("^comment|comments|discuss"))
    rank = html.find_all('span', attrs={'class': re.compile("^rank")})

    return html, point, author, comment, rank

def print_engine(store_all_data):
    """ Creates the output format."""
    print(json.dumps(store_all_data, indent = 2))

an_input = get_user_input()
s_a_d = store_all_data(an_input, HNData)
print_engine(s_a_d)