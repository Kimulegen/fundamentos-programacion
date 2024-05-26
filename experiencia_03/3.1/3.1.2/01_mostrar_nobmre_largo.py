names = []
longest_name = ''
for i in range(3):
    name = input('Ingresa un nombre\n> ')
    names.append(name)
    longest_name = name if len(name) >= len(longest_name) else longest_name

print(f' el nombre más largo es : {longest_name}')

