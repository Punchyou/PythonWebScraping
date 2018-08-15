import hacker_news_scraping as hns
import helping_functions as hf
import unittest
from HN_Data import HNData
from tests_helping_functions import*
import hacker_news_scraping as hns
from bs4 import BeautifulSoup as bs

class TestHNS(unittest.TestCase):
    """ A class for testing the hacker_news_scraping data."""
  
    def test_simple_get_for_valid_html(self):
        """ Tests that the url is a good response."""
        result = hns.simple_get("https://news.ycombinator.com/not-an-html") is None
        self.assertEqual(result, True, "The uri is not a good response.")

    def test_validate_fetched_record_with_valid_data(self):
        """ Tests if all the data are correctly fetched."""
        hn_data_obj = initialize_hn_valid_object()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, True, msg= "One or more data haven't fetched correctly.")

    def test_validate_fetched_record_with_invalid_title_empty(self):
        """ Tests if the title is an empty string."""
        hn_data_obj = initialize_hn_obj_invalid_title_empty()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The title can't be empty.")
    
    def test_validate_fetched_record_with_invalid_title_number(self):
        """ Tests if the title is a number."""
        hn_data_obj = initialize_hn_obj_invalid_title_number()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The title can't be a number.")

    def test_validate_fetched_record_with_invalid_title_too_long(self):
        """ Tests if the title is too long."""
        hn_data_obj = initialize_hn_obj_invalid_title_too_long()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The title can't be more then 256 characters.")
    
    def test_validate_fetched_record_with_invalid_author_name_empty(self):
        """ Tests if the author's name is an empty string."""
        hn_data_obj = initialize_hn_obj_invalid_author_name_empty()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The author's name can't be empty.")
    
    def test_validate_fetched_record_with_invalid_author_name_number(self):
        """ Tests if the author's name is not a number."""
        hn_data_obj = initialize_hn_obj_invalid_author_name_number()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The author's name can't be a number.")

    def test_validate_fetched_record_with_invalid_author_name_too_long(self):
        """ Tests if the author's name is not too long."""
        hn_data_obj = initialize_hn_obj_invalid_author_name_too_long()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The author's name can't be more then 256 characters.")
    
    def test_validate_fetched_record_with_invalid_uri_not_starting_with_http_or_https(self):
        """ Tests if the uri starts with http or https."""
        hn_data_obj = initialize_hn_obj_invalid_uri_not_starting_with_http_or_https()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The uri must start with http or https.")    
    
    def test_validate_fetched_record_with_invalid_uri_domain_name(self):
        """ Tests if the uri domain name has the rights characters."""
        hn_data_obj = initialize_hn_obj_invalid_uri_domain_name()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The uri must start with http or https.")    
    
    def test_validate_fetched_record_with_invalid_points_characters(self):
        """ Tests if the points are characters."""
        hn_data_obj = initialize_hn_obj_invalid_points_character()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The points can't be characters.")
    
    def test_validate_fetched_record_with_invalid_points_negative_number(self):
        """ Tests if the points are a negative number."""
        hn_data_obj = initialize_hn_obj_invalid_points_negative_number()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The points can't be a negative number.")
    
    def test_validate_fetched_record_with_invalid_points_not_integer(self):
        """ Tests if the points are an integer number."""
        hn_data_obj = initialize_hn_obj_invalid_points_not_integer()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The points must be an integer.")
    
    def test_validate_fetched_record_with_invalid_comments_characters(self):
        """ Tests if the numbers of comments are characters."""
        hn_data_obj = initialize_hn_obj_invalid_comments_character()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The points can't be characters.")
    
    def test_validate_fetched_record_with_invalid_comments_negative_number(self):
        """ Tests if the number of comments are a negative number."""
        hn_data_obj = initialize_hn_obj_invalid_comments_negative_number()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The points can't be a negative number.")
    
    def test_validate_fetched_record_with_invalid_comments_not_integer(self):
        """ Tests if the number of comments are an integer number."""
        hn_data_obj = initialize_hn_obj_invalid_comments_not_integer()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The points must be an integer.")
    
    def test_validate_fetched_record_with_invalid_rank_character(self):
        """ Tests if the rank is characters."""
        hn_data_obj = initialize_hn_obj_invalid_rank_character()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The rank can't be characters.")
    
    def test_validate_fetched_record_with_invalid_rank_negative_number(self):
        """ Tests if the rank is a negative number."""
        hn_data_obj = initialize_hn_obj_invalid_rank_negative_number()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The rank can't be a negative number.")
    
    def test_validate_fetched_record_with_invalid_rank_not_integer(self):
        """ Tests if the rank are an integer number."""
        hn_data_obj = initialize_hn_obj_invalid_rank_not_integer()
        result = hf.validate_fetched_record(hn_data_obj)
        self.assertEqual(result, False, msg= "The rank must be an integer.")
    
    def test_store_all_returns_list(self):
        """ Tests that the store_all_data func returns a list of objects."""
        hn_data_obj = initialize_hn_valid_object()
        result = hns.store_all_data(2, hn_data_obj)
        self.assertEqual(isinstance(result, list), True, "The store_all_data doesn't return a list.")
        
"""Provide a command-line interface to the test script."""
unittest.main()