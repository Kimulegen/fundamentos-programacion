#! Python3
# Ask for 3 names, return the longest

# initialize variables
names = []
longest_name = ""

# user inputs 3 names, store longest name
for i in range(3):
    name = input("Ingresa un nombre\n> ")
    names.append(name)
    longest_name = name if len(name) >= len(longest_name) else longest_name

# print longest name
print(f" el nombre más largo es : {longest_name}")
