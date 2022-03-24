from wordle.game import Game
from utils import calculate_guess


def test_new_game():
    game = Game()
    assert len(game.word) == 5
    assert game.lives == 6
    assert not game.game_finished
    assert game.not_in_word == []
    assert game.correct_place == []
    assert game.incorrect_place == []


def test_new_custom_game():
    game = Game('orbit')

    assert len(game.word) == 5
    assert game.lives == 6
    assert not game.game_finished
    assert game.not_in_word == []
    assert game.correct_place == []
    assert game.incorrect_place == []


def test_make_wrong_guess():
    game = Game('risky')
    game.make_guess('orbit')
    assert game.lives == 5


def test_guess_too_long():
    game = Game('risky')
    game.make_guess('guesstoolong')
    assert game.lives == 6


def test_guess_too_short():
    game = Game('risky')
    game.make_guess('ktm')
    assert game.lives == 6


def test_valid_guesses():
    game = Game('orbit')

    game.make_guess('owreb')
    assert game.correct_place == ['O']
    assert game.incorrect_place == ['R', 'B']
    assert game.not_in_word == ['W', 'E']

    game.make_guess('orbzi')
    assert game.correct_place == ['O', 'R', 'B']
    assert game.incorrect_place == ['I']
    assert game.not_in_word == ['W', 'E', 'Z']

    game.make_guess('tibro')
    assert game.correct_place == ['O', 'R', 'B']
    assert game.incorrect_place == ['I', 'T']
    assert game.not_in_word == ['W', 'E', 'Z']


def test_bad_letters():
    game = Game()
    game.not_in_word = ['Q', 'N', 'R']
    words = ['ABUSE', 'NOPLE', 'RIGZY']
    assert calculate_guess(game, words) == ['ABUSE']


def test_good_letters():
    game = Game()
    game.correct_place = ['A']
    game.incorrect_place = ['E', 'R']
    game.not_in_word = ['W', 'T', 'C', 'H', 'I', 'M', 'G', 'D', 'B']
    words = ['Apple', 'Bread', 'Break', 'Laura', 'Layer', 'Paper', 'Trade']
    assert calculate_guess(game, words) == ['Layer', 'Paper']