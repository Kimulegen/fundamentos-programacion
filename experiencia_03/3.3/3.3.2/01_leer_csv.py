#! Python3
# Read a csv, write a json with only adults

import csv
import json

# initialize variables
adults = []

# read csv file, print person's info, add to adults list only people above 18 years of age
with open("datos.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row["Nombre"]
        age = int(row["Edad"])
        district = row["Comuna"]
        age_state = "Mayor de Edad" if age >= 18 else "Menor de Edad"
        print(f"{name} tiene {age} años, es {age_state} y vive en {district}")
        if age > 24:
            adults.append(row)

# write json file with adults list
with open("mayores.json", "w", encoding="utf-8") as file:
    json.dump(adults, file, ensure_ascii=False, indent=1)
