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

## To Use

type in the command line your Github username, password, and the term you want to search

####Example:
```
python search.py (term) -u (username) -p (password)

#if you forgot your password a prompt will show to input your password
python search.py (term) -u (username)
Github Password:
#the input password will not echo in the stdout so it is more secure
```

The result will be saved on a CSV file with a file name of output-YYYY-MM-DD-HH-mm.csv

## Author
**Johnzel Tuddao** - *Initial work* - [J0hnZMT](https://github.com/J0hnZMT)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

