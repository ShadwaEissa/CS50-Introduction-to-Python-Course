def main():
    fuel = input("Fraction: ")
    percentage = convert(fuel)
    print(gauge(percentage))


def convert(fuel):
    while True:
        try:
            num, den = fuel.split("/")
            num = int(num)
            den = int(den)
            fraction = num / den
            if fraction <= 1:
                percentage = fraction * 100
                return percentage
            else:
                fuel = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return ("F")
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()