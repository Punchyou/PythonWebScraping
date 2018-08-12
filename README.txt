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


"""Attempts to get the content at 'url' by making an HTTP GET request.
If the content-type of response is some kind of HTMS/XML, return the text content,
otherwise return None."""
"""Returns True if the response seems to be HTML, False otherwise."""
"""Downloads the page where expected data are found and returns a list of strings."""
""" Finds points, author names, comments and ranks from html."""
""" Makes a list of all the data that retrieved from the html."""
# Creates the desired output format.