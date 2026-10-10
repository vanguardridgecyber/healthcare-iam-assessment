
import csv

with open("data/users.csv", newline="") as file:
    reader = csv.DictReader(file)

    for user in reader:
        print(user["name"])
