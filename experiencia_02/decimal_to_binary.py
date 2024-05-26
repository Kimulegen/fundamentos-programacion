decimal = int(input('Ingrese un numero\n> '))

# RECURSIVE IMPLEMENTATION
def decimal_to_binary(decimal):
    return str(decimal % 2) if decimal <= 1 else decimal_to_binary(decimal // 2) + str(decimal % 2)


print(decimal_to_binary(decimal))

# LOOP IMPLEMENTATION
binary = []
while decimal != 0:
    binary.insert(0,decimal % 2)
    decimal = decimal // 2
    
print("".join(map(str, binary)))

