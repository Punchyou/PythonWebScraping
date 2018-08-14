import hacker_news_scraping as hns
import helping_functions as hf
import unittest

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
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, True, msg= "One or more fetched data don't have the required form.")
        result = hf.validate_fetched_record(
            7, "Maria", "https://news.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "Title must be a string.")
        result = hf.validate_fetched_record(
            "", "Maria", "https://news.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "Title can't be an empty string.")
        result = hf.validate_fetched_record(
            "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there,I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon.", "Maria", "https://news.ycombinator.com/",  23, 4, 3)
        self.assertEqual(result, False, msg= "Title can't be more than 256 characters.")

    def test_validate_fetched_record_author_name(self):
        """ Tests if the fetched author name has the proper form."""
        result = hf.validate_fetched_record(
            85, "Maria", "https://news.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "Author's name must be a string.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "", "https://news.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "Author's name can't be an empty string.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there,I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon.", "https://news.ycombinator.com/",  23, 4, 3)
        self.assertEqual(result, False, msg= "Author's name can't be more than 256 characters.")

    def test_validate_fetched_record_URI(self):
        """ Tests if the fetched URI has the proper form."""
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "hthk://news.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "The URI must start with http:// or https://.")
        result = hf.validate_fetched_record(
            "Sharlock Holmes", "Maria", "https:/news.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "The URI must start with http:// or https://.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news#.ycombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "The domain name can contain only letters and numbers.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "hthk://news.yc ombinator.com/", 23, 4, 3)
        self.assertEqual(result, False, msg= "The domain name can't contain spaces.")

    def test_validate_fetched_record_points(self):
        """ Tests if the fetched points has the proper form."""
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", "23", 4, 3)
        self.assertEqual(result, False, msg= "Points must be a number.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23.2, 4, 3)
        self.assertEqual(result, False, msg= "Points must be an integer number.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", -1, 4, 3)
        self.assertEqual(result, False, msg= "Points must be positive numbers or 0.")    
    
    def test_validate_fetched_record_comments(self):
        """ Tests if the fetched number of comments has the proper form."""
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23, "4", 3)
        self.assertEqual(result, False, msg= "Comments must be a number.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23, 4.2, 3)
        self.assertEqual(result, False, msg= "Comments must be an integer number.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23, -4, 3)
        self.assertEqual(result, False, msg= "Comments must be positive integers or 0.")

    def test_validate_fetched_record_rank(self):
        """ Tests if the fetched ranking number has the proper form."""
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23, 4, "3")
        self.assertEqual(result, False, msg= "Rank must be a number.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23, 4, 3.2)
        self.assertEqual(result, False, msg= "Rank must be an integer number.")
        result = hf.validate_fetched_record(
            "Sherlock Holmes", "Maria", "https://news.ycombinator.com/", 23, 4, -33)
        self.assertEqual(result, False, msg= "Rank must a positive integer or 0.")
        

        

def test_add(self):
    # This is how a simple test method should look like.
    result = hns.add(10, 5)
    self.assertEqual(result, 15)

"""Provide a command-line interface to the test script."""
unittest.main()