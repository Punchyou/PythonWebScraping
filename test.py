import hacker_news_scraping as hns
import helping_functions as hf
import unittest
from HN_Data import HNData

#unittest: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

"""Test the simple_get without using unittest"""

'''raw_html = simple_get("https://news.ycombinator.com/")
print(len(raw_html))

no_html = simple_get("https://news.ycombinator.com/not-an-html")
print(no_html is None)'''

class TestHNS(unittest.TestCase):
    """ A class for testing the hacker_news_scraping data."""
    def test_validate_fetched_record_title(self):
        """ Tests if the fetched name has the proper form."""
        HNData().title = "lkdjfglkj"
        result = hf.validate_fetched_record(HNData())
        self.assertEqual(result, True, msg= "One or more fetched data don't have the required form.")
        
        

def test_add(self):
    # This is how a simple test method should look like.
    result = hns.add(10, 5)
    self.assertEqual(result, 15)

"""Provide a command-line interface to the test script."""
unittest.main()