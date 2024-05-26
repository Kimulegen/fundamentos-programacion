bricks_used = 0
number_of_bricks = 6
floor = 0

while bricks_used <= number_of_bricks:
    floor += 1
    bricks_used = bricks_used + floor
    

print(floor - 1)