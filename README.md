# Search Github
Machine Problem: GitHub API

A CLI application which takes in a search term and searches GitHub repositories for that term.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

First you need to install the gdeck package to use as a module

#### To install using pip

```
pip install gdeck
```
#### To install using pipenv

```
pipenv install gdeck
```

## Running the tests

To test the module you can run any of the following:

### using pytest command

```
pytest --cov=gdeck

```
### using py.test command

```
py.test --cov=gdeck

```
### running any test file in the directory

```
python -m pytest --cov=gdeck

```

## To Use

import the gdeck module then instantiate the Card or Deck class to use
####Example:
```
import gdeck

card = gdeck.Card(rank, suit)
deck = gdeck.Deck()

```

### To use the Card
 ```
rank = 5
suit = Hearts

card = gdeck.Card(rank, suit)

```
You can only use the four suits in the deck of cards 'Hearts', 'Clubs', 'Diamonds' or 'Spades'.Card

###To use the Deck
 ```
deck = gdeck.Deck()
# to display the 52 cards in the deck
deck.show()
# to display only n number of cards
deck.show(5)#this will print only 5 sets of cards
#you can also shuffle the deck
deck.shuffle()#this will only shuffle the deck but will not display the cards
#you can also draw the first card on the deck
deck.draw_top()#this will draw the first card on the deck
#you can also draw any random card on the deck
deck.choice()#this will draw 1 any random card
deck.choice(5)#this will draw 5 any random card
#you can also use slicing to get a set of cards from the deck
deck[0:52]#this will display all the cards on the deck
deck[0:10]#this will display only the first 10 cards on the deck
```
--the Deck is also an iterator so you can use it on next() function or in random() function

## Author
**Johnzel Tuddao** - *Initial work* - [J0hnZMT](https://github.com/J0hnZMT)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

