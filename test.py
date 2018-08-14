import hacker_news_scraping as hns
import helping_functions as hf
import unittest
from HN_Data import HNData

def initialize_hn_valid_object():
    hn_data_obj = HNData("Sherlock", "Doyle", "ttps://news.ycombinator.com/", 34, 20, 3)
    return hn_data_obj

def initialize_hn_obj_invalid_title():
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.title = ""
    return hn_data_obj

def initialize_hn_obj_invalid_author():
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.author = ""
    return hn_data_obj

"""Test the simple_get without using unittest"""

'''raw_html = simple_get("https://news.ycombinator.com/")
print(len(raw_html))

no_html = simple_get("https://news.ycombinator.com/not-an-html")
print(no_html is None)'''

class TestHNS(unittest.TestCase):
    """ A class for testing the hacker_news_scraping data."""
    def test_validate_fetched_record_with_invalid_title(self):
        
        """Arrange"""
        hn_data_obj = initialize_hn_obj_invalid_title()

        """Act"""
        result = hf.validate_fetched_record(hn_data_obj)

        """Assert"""
        self.assertEqual(result, True, msg= "One or more fetched data don't have the required form.")
        
        

def test_add(self):
    # This is how a simple test method should look like.
    result = hns.add(10, 5)
    self.assertEqual(result, 15)

"""Provide a command-line interface to the test script."""
unittest.main()