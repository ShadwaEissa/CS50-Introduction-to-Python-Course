from plates import is_valid

def test_length():
    assert is_valid("ABCDE") == True
    assert is_valid("AB") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_firsttwoletters():
    assert is_valid("AB") == True
    assert is_valid("A2") == False

def test_zeroplacement():
    assert is_valid("AB0123") == False
    assert is_valid("ABF123") == True

def test_numberplacement():
    assert is_valid("ABC123") == True
    assert is_valid("AB512C") == False
    assert is_valid("A1512V") == False

def test_alphanumeric():
    assert is_valid("ABC123") == True
    assert is_valid("ABC1!") == False