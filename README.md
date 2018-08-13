# Web scraping with Python

This is a repo about basic web scraping, with Python. This application uses the BeautifulSoup python library to retrieve specific data from a website and output the top posts.

## Installation

You'll have to install Python 3.7 on your system. Download the appropriate for your OS installer from https://www.python.org/downloads/release/python-370/.

You'll install the packages needed for this project with the pip installer that allows you to install, reinstall, or uninstall PyPI packages, which is already installed with Python 3.7.

The packages you'll need are:

** Requests


### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

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
