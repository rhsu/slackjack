from utils.color_util import determine_color


def test_1_10_even():
    assert determine_color(1) == "red"

def test_1_10_odd():
    assert determine_color(10) == "black"

def test_19_28_even():
    assert determine_color(28) == "black"

def test_19_28_odd():
    assert determine_color(19) == "red"
