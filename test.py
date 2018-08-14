import hacker_news_scraping as hns
import helping_functions as hf
import unittest
from HN_Data import HNData

def initialize_hn_valid_object():
    """Initialize the data object with valid data."""
    hn_data_obj = HNData("Sherlock", "Doyle", "ttps://news.ycombinator.com/", 34, 20, 3)
    return hn_data_obj

def initialize_hn_obj_invalid_title_empty():
    """ Initialize an object with invalid title, an empty string."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.title = ""
    return hn_data_obj

def initialize_hn_obj_invalid_title_number():
    """ Initialiaze an object with invalid title, a number."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.title = 7
    return hn_data_obj

def initialize_hn_obj_invalid_title_too_long():
    """Initialiaze an object with invalid title, with too many characters."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.title = "I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the home-centred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes..."
    return hn_data_obj

def initialize_hn_obj_invalid_author_name_empty():
    """ Initialize an object with invalid author's name, an empty string."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.author = ""
    return hn_data_obj

def initialize_hn_obj_invalid_author_name_number():
    """ Initialize an object with invalid author's name, a number."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.author = 7
    return hn_data_obj

def initialize_hn_obj_invalid_author_name_too_long():
    """ Initialize an object with invalid author's name, too many charasters."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.author = "I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the home-centred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes..."
    return hn_data_obj




"""Test the simple_get without using unittest"""

'''raw_html = simple_get("https://news.ycombinator.com/")
print(len(raw_html))

no_html = simple_get("https://news.ycombinator.com/not-an-html")
print(no_html is None)'''

class TestHNS(unittest.TestCase):
    """ A class for testing the hacker_news_scraping data."""

    def test_validate_fetched_record_with_valid_data(self):
        hn_data_obj = initialize_hn_valid_object()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, True, msg= "One or more data haven't fetched correctly.")

    def test_validate_fetched_record_with_invalid_title_empty(self):
        hn_data_obj = initialize_hn_obj_invalid_title_empty()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The title can't be empty.")
    
    def test_validate_fetched_record_with_invalid_title_number(self):
        hn_data_obj = initialize_hn_obj_invalid_title_number()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The title can't be a number.")

    def test_validate_fetched_record_with_invalid_title_too_long(self):
        hn_data_obj = initialize_hn_obj_invalid_title_too_long()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The title can't be more then 256 characters.")
    
    def test_validate_fetched_record_with_invalid_author_name_empty(self):
        hn_data_obj = initialize_hn_obj_invalid_author_name_empty()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The author's name can't be empty.")
    
    def test_validate_fetched_record_with_invalid_author_name_number(self):
        hn_data_obj = initialize_hn_obj_invalid_author_name_number()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The author's name can't be a number.")

    def test_validate_fetched_record_with_invalid_author_name_too_long(self):
        hn_data_obj = initialize_hn_obj_invalid_author_name_too_long()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The author's name can't be more then 256 characters.")
        
        
"""Provide a command-line interface to the test script."""
unittest.main()