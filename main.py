from wordle.game import Game


game = Game()

print('''
+----------------  New Wordle Game Started  ---------------+
|                                                          |
|          You have 6 tries to guess a 5 letter word       |
|                                                          |
|           Each guess must be valid 5 letter word         |
|                                                          |
|                      Good luck.                          |
|                                                          |
+----------------------------------------------------------+
''')

while not game.game_finished and game.lives > 0:
    guess = input('Enter your guess:   ')
    game.make_guess(guess)
    if not game.game_finished:
        print(f'''
        Letters in correct places guessed:      {' '.join(game.correct_place)}
        Correct letter, but incorrect place:    {' '.join(game.incorrect_place)}
        Letters not in word:                    {' '.join(game.not_in_word)}
        
        Lives left: {game.lives}
        ''')
if game.lives == 0:
    print(f'''
    No more lives. Better luck next time.
    
    Answer was:  {game.word}
    ''')
