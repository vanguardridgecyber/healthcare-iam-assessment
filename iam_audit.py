
import csv

with open("data/users.csv", newline="") as file:
    reader = csv.DictReader(file)

    for user in reader:
        if user["employment_status"] == "terminated":
           if user["account_status"] == "active":
              print("SECURITY ALERT:", user["name"])
