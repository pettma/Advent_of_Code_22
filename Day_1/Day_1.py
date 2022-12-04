# current_max = 0
# condition = True
# count = 0
# currentelfline = 0
#   
# while condition
#   readline(count)
#   if line = empty
#       sum = inputline length current elf
#   currentelfline + 1
#   sum = sum + input

elves_cal = []

with open('/Users/pettermartinussen/CS/Advent_of_Code_22/Day_1/Day_1/input.txt') as f:
    for line in f:
        elves_cal.append(line)

current_max = 0
current_sum = 0
current_elf = 0
max_elf = 0

for i in elves_cal:
    if i.strip() == '':
        if current_sum > current_max:
            current_max = current_sum
            max_elf = current_elf
            current_elf += 1
            current_sum = 0
        else:
            current_elf += 1
            current_sum = 0
    else:
        current_sum = current_sum + int(float(i))

print('Elf number ' + str(current_elf + 1) + ' is carrying the most calories. It carries ' + str(current_max) + ' calories')