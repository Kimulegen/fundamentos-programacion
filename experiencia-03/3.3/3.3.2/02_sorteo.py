#! Python3
# Stores raffle winners

import csv
import json

# initialize variables
winners = []

# read csv file, if person's run ends with 92,95, or 84, store them in winners list
with open("listadoRun.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        last_two_digits = int(row["run"][-4:-2])
        if last_two_digits in {92, 95, 84}:
            winners.append(row)


# write json file with raffle winners
with open("ganadores.json", "w", encoding="utf-8") as file:
    json.dump(winners, file, indent=1, ensure_ascii=False)
