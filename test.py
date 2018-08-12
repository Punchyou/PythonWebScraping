from hacker_news_scraping import*
import unittest

#unittest: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

"""Test the simple_get without using unittest"""

raw_html = simple_get("https://news.ycombinator.com/")
print(len(raw_html))

no_html = simple_get("https://news.ycombinator.com/not-gonna-find-it")
print(no_html is None)

class TestHNS(unittest.TestCase):
    """ A class for testing the hacker_news_scraping methods."""

    def test_is_good_response(self):
        # Tests the is_good_response method.
        pass
    
    def test_log_error(self):
        # Tests the log_error method.
        pass

    def test_get_all_data(self):
        # Tests the get_all_data method.
        pass

    def test_find_data(self):
        # Tests the find_data method.
        pass    
    
    def test_make_list_of_HNdata_dicionaries(self):
        # Tests the find_all_data method.
        pass



def test_add(self):
    # This is how a simple test method should look like.
    result = add(10, 5)
    self.assertEqual(result, 15)

# Provide a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()