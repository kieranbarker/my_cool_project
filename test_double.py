from helpers import double


def test_double():
    assert double(2) == 4


def test_string_double():
    assert double("hello") == "ERROR"
