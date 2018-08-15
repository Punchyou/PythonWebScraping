# Web scraping with Python

This is a repo about basic web scraping, with Python. This application uses the BeautifulSoup python library to retrieve specific data from a website and output the top posts.

## Installation

You'll have to install Python 3.7 on your system. Download the appropriate for your OS installer from https://www.python.org/downloads/release/python-370/.

You'll install the packages needed for this project with the pip installer that allows you to install, reinstall, or uninstall PyPI packages. Pip is already installed with Python 3.7.


### The packages you'll need are:

**requests**

Requests library is designed to be used by humans to interact with the language. We need it in the project to get the content at 'url' by making an HTTP GET request, with requests.get() function.

To install this module, type on your terminal:
```
pip install requests
```
For this packages (and for the next packages),
```
pip3 install requests
```
might also work.

**contextlib**

Contextlib provides utilities for common tasks involving the with statement, that "sets things up" and "tear things down" automatically, when needed. The contextlib.closing() function is used here to ensure that any network resources are freed when they go out of scope in a with block.

For installation:
```
pip install contectlib
```

**bs4**

Beautiful Soup library is a toolkit for dissecting a document and extracting what you need. We ned the bs4.BeautifulSoup function to parse the HTML.

Type on your terminal
```
pip install bs4
```
to install it.

**re**

We need the re regular expressions in this project returns the "compiled" regular expression object with re.compiled() function, which find_all consumes.

Type on your terminal
```
pip install re
```
to install it.

**json**

We need the json library here, for storing the data in the JSON format, with the json.dumps() function.

Type on your terminal
```
pip install json
```
to install it.

**collections**
This module implements specialized container alternative datatypes. We need the collections.OrderedDict() function to initialize an ordered dictionary.

The main file of this project is hacker_news_scraping.py. Type "py hacker_news_scraping.py" in a terminal, to run it. Type also "py test.py" to run the tests.
