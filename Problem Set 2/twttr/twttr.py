x = input("Input: ")

vowels = ["a", "i", "e", "o", "u", "A", "I", "E", "O", "U"]

for i in x:
    if i in vowels:
        x = x.replace(i, "")

print(x)
