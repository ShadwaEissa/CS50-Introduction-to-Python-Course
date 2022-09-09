x = input("Expression: ")
first_num = int(x.split()[0])
second_num = int(x.split()[2])
sign = x.split()[1]

if "+" in sign:
    result = first_num + second_num
    print(f"{result:.1f}")

elif "-" in sign:
    result = first_num - second_num
    print(f"{result:.1f}")

elif "*" in sign:
    result = first_num * second_num
    print(f"{result:.1f}")

elif "/" in sign:
    result = first_num / second_num
    print(f"{result:.1f}")
