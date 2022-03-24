from wordle.game import Game
from utils import calculate_guess

import time
import random as r

game = Game()

with open('wordle/word_list.txt') as f:
    words = f.read().splitlines()

while not game.game_finished and game.lives > 0:
    time.sleep(1)
    calculate_guess(game, words)
    guess = words[r.randint(0, len(words)-1)]
    print(f'Attempting to guess with:   {guess.upper()}..')
    game.make_guess(guess)

    if not game.game_finished:
        print(f'''
        Letters in correct places guessed:      {' '.join(game.correct_place)}
        Correct letter, but incorrect place:    {' '.join(game.incorrect_place)}
        Letters not in word:                    {' '.join(game.not_in_word)}

        Lives left: {game.lives}
        ''')

if game.lives == 0:
    print(f'No more lives.')
    time.sleep(2)
    print('This is a very bad autosolver..')
    time.sleep(2)
    print(f'Answer was:  {game.word}')
else:
    time.sleep(2)
    print('\n Good autosolver.')