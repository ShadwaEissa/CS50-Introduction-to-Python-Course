import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    sentence = re.findall(r"\bum\b", s, re.IGNORECASE)
    count = len(sentence)
    return count

if __name__ == "__main__":
    main()