from bank import value

def test_string_lowercase():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("cat") == 100

def test_string_uppercase():
    assert value("HELLO") == 0

def test_string_numbers():
    assert value("123") == 100
