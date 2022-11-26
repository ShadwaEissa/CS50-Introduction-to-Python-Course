import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"^<iframe(.)*><\/iframe>$", s):
        if matches := re.search(r"http(s)?:\/\/(www\.)?youtube\.com\/embed\/([a-zA-Z0-9]+)", s):
            code = matches.group(3)
            return "https://youtu.be/" + code


if __name__ == "__main__":
    main()