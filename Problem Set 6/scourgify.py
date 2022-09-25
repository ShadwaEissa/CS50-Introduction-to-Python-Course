import csv
import sys

students = []

if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(",")
                    students.append({"firstname":first.lstrip(), "lastname":last, "address":row["house"]})
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames = ["a", "b", "c"])
                writer.writerow({"a":"first", "b":"last", "c":"house"})
                for student in students:
                    writer.writerow({"a":student["firstname"], "b":student["lastname"], "c":student["address"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")