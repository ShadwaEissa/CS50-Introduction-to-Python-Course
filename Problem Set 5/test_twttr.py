from twttr import shorten

def test_lowercases():
    assert shorten("twitter") == "twttr"
    assert shorten("play") == "ply"

def test_uppercases():
    assert shorten("CAT") == "CT"
    assert shorten("DOG") == "DG"

def test_numbers():
    assert shorten("1234") == "1234"

def test_punctuations():
    assert shorten(".!?") == ".!?"
