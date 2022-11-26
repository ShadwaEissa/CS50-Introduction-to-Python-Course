from um import count

def main():
    test_spaces_around()
    test_case_insensitive()
    test_in_words()

def test_spaces_around():
    assert count("Hello, um MO?") == 1
    assert count("shady, um shadwa, um Aboody?") == 2

def test_case_insensitive():
    assert count("UM no?") == 1
    assert count("thanks, Um very much") == 1

def test_in_words():
    assert count("I like this album") == 0
    assert count("equilibrium") == 0

