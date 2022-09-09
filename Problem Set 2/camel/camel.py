camelCase = input("camelCase: ")
print("snake_case: ", end="")

for x in camelCase:
    if x.isupper():
        print("_" + x.lower(), end="")
    else:
        print(x, end="")

print()