from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False
    assert validate("cat") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("255.522.255.255") == False
    assert validate("522.255.255.255") == False

if __name__ == "__main__":
    main()
