from utils.hand_util import (
    hand_string,
    hand_sum
)


def test_hand_string(some_busted_hand):
    result = hand_string(some_busted_hand)
    assert result == "Q :spades: K :spades: J :spades:"


def test_hand_sum(some_busted_hand):
    result = hand_sum(some_busted_hand)
    assert result == 30


def test_black_jack(black_jack_hand):
    result = hand_sum(black_jack_hand)
    assert result == 21
