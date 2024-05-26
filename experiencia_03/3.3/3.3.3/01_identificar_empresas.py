import csv, json

segmentation = {
    'minor_contributor': [],
    'medium_contributor': [],
    'large_contributor': []
}
with open('listadoRutEmpresa.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    updated_data = []
    for row in reader:
        sales = int(row['ventas'])
        if sales <= 100000000:
            segmentation['minor_contributor'].append(row)
            row['clasificacionEmpresa'] = 'Pequeño Contribuyente'
            updated_data.append(row)
            
        elif sales <=200000000:
            segmentation['medium_contributor'].append(row)
            row['clasificacionEmpresa'] = 'Mediano Contribuyente'
            updated_data.append(row)
        else:
            segmentation['large_contributor'].append(row)
            row['clasificacionEmpresa'] = 'Gran Contribuyente'
            updated_data.append(row)


with open('listadoRutEmpresa.csv', 'w', newline='') as file:
    fieldnames = fieldnames + ['clasificacionEmpresa']
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()

    writer.writerows(updated_data)
    
    

        
with open('segmentacionEmpresas.json', 'w') as json_file:
    json.dump(segmentation, json_file, indent=1, ensure_ascii=False)