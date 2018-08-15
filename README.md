# Web scraping with Python

This is a repo about basic web scraping, with Python. This application uses the BeautifulSoup python library to retrieve specific data from a website and output the top posts.

## Installation

You'll have to install Python 3.7 on your system. Download the appropriate for your OS installer from https://www.python.org/downloads/release/python-370/.

You'll install the packages needed for this project with the pip installer that allows you to install, reinstall, or uninstall PyPI packages. Pip is already installed with Python 3.7.


### The packages you'll need are:

**Requests**

Requests is an Apache2 Licensed HTTP library, written in Python. It is designed to be used by humans to interact with the language. This means you don’t have to manually add query strings to URLs, or form-encode your POST data. We need it in the project to get the content at 'url' by making an HTTP GET request, with requests.get() function.
```
pip install requests
```
or
```
pip3 install requests
```
might also work.

**Contextlib**

Contextlib provides utilities for common tasks involving the with statement, that "sets things up" and "tear things down" automatically, when needed. The contextlib.closing() function is used here to ensure that any network resources are freed when they go out of scope in a with block.

**bs4**

Beautiful Soup library is a toolkit for dissecting a document and extracting what you need. We use the bs4.BeautifulSoup function to parse the HTML.

**Re**

We use here the re Regular expressions in this project returns the "compiled" regular expression object with re.compiled() function, which find_all consumes.

**json**


### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

---To be continued

Info

The simple_get() attempts to get the content at 'url' by making an HTTP GET request.
The closing() function ensures that any network resources are freed when they go out of scope in that with block.

To start selecting and extracting, we use the BeautifulSoup library. 
The BeautifulSoup constructor parses raw HTML strings and produces an object that mirrors the HTML document’s structure.
The standard back-end parser is 'html.parser'.

The use of json.dumps is for pretty printing the data.

"""Returns True if the response seems to be HTML, False otherwise."""
"""Downloads the page where expected data are found and returns a list of strings."""
""" Finds points, author names, comments and ranks from html."""
""" Makes a list of all the data that retrieved from the html."""
print_engine() Creates the desired output format.

Type "python hacker_news_scraping.py" in a terminal, to run.
