months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except:
        try:
            oldmonth, oldday, year = date.split(" ")
            for i in range(len(months)):
                if oldmonth == months[i]:
                    month = i + 1
            if oldday.endswith(","):
                day = oldday.replace(",","")
                if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                    break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
