while True:
    try:
        tank = input("Fraction: ")
        #checking that inputs are integers
        num, den = [int(x) for x in tank.split("/")]
        #checking that num. < den. and den. not 0
        if num <= den and den != 0:
            break
    except (ValueError, ZeroDivisionError):
        pass 

f = num / den
p = round(f * 100)

if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
