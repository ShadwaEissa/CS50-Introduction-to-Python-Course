import emoji

input = input("Input: ")

if len(input) > 1:
    start = input.index(":")
    end = input.index(":", start + 1)
    input = input[start: end +1]

print("Output: ", emoji.emojize(input, language="alias"))