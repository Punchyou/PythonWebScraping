from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re
from pprint import pprint
import inspect
from collections import OrderedDict
import json
#Your first task will be to download web pages.
# The requests package comes to the rescue.
# It aims to be an easy-to-use tool for doing all things HTTP in Python.

#The simple_get() function accepts a single url argument.
# It then makes a GET request to that URL.
# If nothing goes wrong, you end up with the raw HTML content for the page you requested.
# If there were any problems with your request (like the URL is bad, or the remote server is down), then your function returns None.
# You may have noticed the use of the closing() function in your definition of simple_get().
# The closing() function ensures that any network resources are freed when they go out of scope in that with block.
# Using closing() like that is good practice and helps to prevent fatal errors and network timeouts.

#Once you have raw HTML in front of you, you can start to select and extract.
# For this purpose, you will be using BeautifulSoup.
# The BeautifulSoup constructor parses raw HTML strings and produces an object that mirrors the HTML document’s structure.
# The object includes a slew of methods to select, view, and manipulate DOM nodes and text content.

#BeautifulSoup accepts multiple back-end parsers, but the standard back-end is 'html.parser',
# which you supply here as the second argument.

#The select() method on your html object lets you use CSS selectors to locate elements in the document.
# In the above case, html.select('p') returns a list of paragraph elements.
# Each p has HTML attributes that you can access like a dict. In the line if p['id'] == 'walrus', for example,
# you check if the id attribute is equal to the string 'walrus', which corresponds to <p id="walrus"> in the HTML.

#Use json.dumps to pretty print your data

def simple_get(url):
    """Attempts to get the content at 'url' by making an HTTP GET request.
    If the content-type of response is some kind of HTMS/XML, return the text content,
    otherwise return None."""

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
    """Prints the log errors"""
    print(e)

def store_all_data():
    """Downloads the page where expected data are found
    and returns a list of strings."""

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
    # Finds points, author names, comments and ranks from html.
    point = html.find_all('span', attrs={'class': re.compile("^scor")})
    author = html.find_all('a', attrs={'href': re.compile("^user")})
    comment = html.find_all('a', text= re.compile("comment|comments|discuss"))
    rank = html.find_all('span', attrs={'class': re.compile("^rank")})

    return html, point, author, comment, rank

def make_list_of_HNdata_dictionaries(input_number, html, points, authors, comments, ranks):
    # Makes a list of all the data that retrieves from the html.
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

    '''for i in hacker_news_list:
        print(i)
    return hacker_news_list'''

#def make_output_form():

def print_engine(store_all_data):
    # Makes the desires output format.
    print("[")
    for d in store_all_data():
        print(json.dumps(d, indent=1) + "," if d != store_all_data()[-1] else json.dumps(d, indent=1))
    print("]")

print_engine(store_all_data)

def add(x,y):
    return x + y