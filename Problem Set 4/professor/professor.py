import random

def main():
    l = get_level()
    generate_integer(l)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break  
        except ValueError:
            pass
    return level

def generate_integer(level):
    score = 0
    if level == 1:
        for i in range(10):
            x = random.randint(0,9)
            y = random.randint(0,9)
            input_answer = int(input(f"{x} + {y} = "))
            answer = int(x + y)
            if input_answer == answer:
                score += 1
            else:
                print("EEE")
                i = 0
                while i != 2:
                    input_answer = int(input(f"{x} + {y} = "))
                    if input_answer != answer:
                        print("EEE")
                        i += 1
                    else:
                        break
                print(f"{x} + {y} = {answer}")
        print("Score:",score)
    elif level == 2:
        for i in range(10):
            x = random.randint(10,99)
            y = random.randint(10,99)
            input_answer = int(input(f"{x} + {y} = "))
            answer = int(x + y)
            if input_answer == answer:
                score += 1
            else:
                print("EEE")
                i = 0
                while i != 2:
                    input_answer = int(input(f"{x} + {y} = "))
                    if input_answer != answer:
                        print("EEE")
                        i += 1
                    else:
                        break
                print(f"{x} + {y} = {answer}")
        print("Score:",score)
    elif level == 3:
        for i in range(10):
            x = random.randint(100,999)
            y = random.randint(100,999)
            input_answer = int(input(f"{x} + {y} = "))
            answer = int(x + y)
            if input_answer == answer:
                score += 1
            else:
                print("EEE")
                i = 0
                while i != 2:
                    input_answer = int(input(f"{x} + {y} = "))
                    if input_answer != answer:
                        print("EEE")
                        i += 1
                    else:
                        break
                print(f"{x} + {y} = {answer}")
        print("Score:",score)


if __name__ == "__main__":
    main()