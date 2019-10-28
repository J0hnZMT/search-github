# Search Github
Machine Problem: GitHub API

A CLI application which takes in a search term and searches GitHub repositories for that term.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

First you need to install the requests package

#### Install using pipenv

```
pipenv install requests
```

## Running the tests

To test the module you can run any of the following:

### using pytest command

```
pytest --cov=search

```

## To Use

type in the command line your Github username, password, and the term you want to search

####Example:
```
python search.py (Username) (password) (term)
```

The result will be saved on a CSV file with a file name of output-YYYY-MM-DD-HH-mm.csv

## Author
**Johnzel Tuddao** - *Initial work* - [J0hnZMT](https://github.com/J0hnZMT)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

