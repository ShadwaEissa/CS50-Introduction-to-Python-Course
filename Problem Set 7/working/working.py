import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    checking = re.search(r"^([0-9]+):*([0-9]*) (AM|PM) to ([0-9]+):*([0-9]*) (AM|PM)$", s)
    if checking:
        list = checking.groups()
        if int(list[0]) > 12 or int(list[3]) > 12:
            raise ValueError
        fromtime = newformat(list[0], list[1], list[2])
        totime = newformat(list[3], list[4], list[5])
        return fromtime + " to " + totime
    else:
        raise ValueError


def newformat(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            newhour = 12
        else:
            newhour = int(hour) + 12
    else:
        if int(hour) == 12:
            newhour = 0
        else:
            newhour = int(hour)
    if minute == "":
        newminute = ":00"
        newtime = f"{newhour:02}" + newminute
        return newtime
    elif int(minute) > 59:
        raise ValueError
    else:
        newtime = f"{newhour:02}" + ":" + minute
        return newtime

if __name__ == "__main__":
    main()