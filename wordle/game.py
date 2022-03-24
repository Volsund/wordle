import random as r


class Game:
    def __init__(self, word: str = None):
        self.lives = 6
        self.game_finished = False
        self.correct_place = []
        self.incorrect_place = []
        self.not_in_word = []
        if word is None:
            with open('wordle/word_list.txt') as f:
                words = f.read().splitlines()
                self.word = words[r.randint(0, len(words)-1)].upper()
        else:
            self.word = word.upper()

    def make_guess(self, guess: str):
        guess = guess.upper()
        if len(guess) == len(self.word):
            if guess == self.word:
                print('~~~~ CONGRATULATIONS! That is correct! ~~~~')
                self.game_finished = True
            else:
                if self.lives > 0:
                    self.sort_letters(guess)
                    self.lives -= 1
                else:
                    self.game_finished = True
        else:
            print(f'Guess must be {len(self.word)} letters long!')

    def sort_letters(self, guess: str):
        for pos in range(len(guess)):
            if guess[pos] in self.word:
                # If letter has correct place guessed
                if guess[pos] == self.word[pos]:
                    if guess[pos] not in self.correct_place:
                        self.correct_place.append(guess[pos])
                    if guess[pos] in self.incorrect_place:
                        self.incorrect_place.remove(guess[pos])
                # If letter is in the word, but incorrect place
                else:
                    if guess[pos] not in self.incorrect_place \
                            and guess[pos] not in self.correct_place:
                        self.incorrect_place.append(guess[pos])
            # Letter not in the word
            else:
                if guess[pos] not in self.not_in_word:
                    self.not_in_word.append(guess[pos])
