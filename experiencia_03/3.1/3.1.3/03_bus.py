#! Python3
# print the sits of a bus

# initialize variables
bus = []
sit_number = 1

# build bus, each sit is represented as a number
for i in range(10):
    row = []
    for j in range(4):
        sit = "{:02d}".format(i*4 + j+ 1)
        row.append(sit)
    bus.append(row)

# show formatted bus matrix
for row in bus:
    for i,item in enumerate(row):
        print(item, end=' ')
        if i == 1:
            print('    ', end='')
    print()
