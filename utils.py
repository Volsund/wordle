from wordle.game import Game


def calculate_guess(game: Game, words: [str]):
    possible_words = words

    good_letters = game.incorrect_place + game.correct_place
    bad_letters = game.not_in_word

    if bad_letters:
        for letter in bad_letters:
            for word in possible_words:
                if letter in word.upper():
                    possible_words.remove(word)

    if good_letters:
        for letter in good_letters:
            for word in possible_words:
                if letter not in word.upper():
                    possible_words.remove(word)
                    pass

    return possible_words