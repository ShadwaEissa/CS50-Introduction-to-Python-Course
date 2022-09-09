def main():
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):
    vowels = ["a", "i", "e", "o", "u", "A", "I", "E", "O", "U"]
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()