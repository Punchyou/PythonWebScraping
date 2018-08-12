from collections import OrderedDict
import re

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