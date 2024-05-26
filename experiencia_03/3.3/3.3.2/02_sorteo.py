import csv
import json

winners = []
with open('listadoRun.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        last_two_digits = int(row['run'][-4:-2])
        if last_two_digits in {92,95,84}:
            winners.append(row)


with open('ganadores.json', 'w', encoding='utf-8') as file:
    json.dump(winners, file, indent=1, ensure_ascii=False)