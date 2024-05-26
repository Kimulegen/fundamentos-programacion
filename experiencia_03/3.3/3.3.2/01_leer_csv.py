import csv
import json

adults = []
with open('datos.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row['Nombre']
        age = int(row['Edad'])
        district = row['Comuna']
        age_state = 'Mayor de Edad' if age >= 18 else 'Menor de Edad'
        print(f'{name} tiene {age} años, es {age_state} y vive en {district}')
        if age > 24:
            adults.append(row)

with open('mayores.json', 'w', encoding='utf-8') as file:
    json.dump(adults, file, ensure_ascii=False, indent=1)