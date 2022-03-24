# wordle

Based on [NY Times wordle](https://www.nytimes.com/games/wordle/index.html).  
Words are taken from text file for reliability purposes, but it can be replaced by existing PyPi packages or APIs.  
Can be played via console or using autosolver.

### Setup

1. Clone repository
2. `python3.8 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`

### Usage
- To run tests: `pytest`
- To play the game via console: `python main.py`
- To use autosolver via console: `python autosolver.py`

### To Do
- Autosolver currently checks if words consist of found letters and ignores words with  'bad letters', but it also should check if found letters is in correct place, which would significantly improve solving time/chances.
- Improve visual represantation for each guessing round.
