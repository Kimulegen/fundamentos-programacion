names = []
longest_name = ''
for i in range(3):
    name = input("Ingrese un nombre")
    longest_name = name if len(name)>len(longest_name) else longest_name

print(f"El nombre mas largo es {longest_name}")