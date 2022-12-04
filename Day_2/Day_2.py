# Rock      - A     - X     - 1 point
# Paper     - B     - Y     - 2 points
# Scissors  - C     - Z     - 3 points

# Win   - 6 points
# Draw  - 3 points
# Lose  - 0 points

# iterate through file
# check line with boolean logic
# sum points

def check_points(a, b):
    points = 0

    if a == 'A':                # Opponent chooses Rock
        if b == 'X':            # You choose rock
            points = 1 + 3
        elif b == 'Y':          # You choose Paper
            points = 2 + 6
        elif b == 'Z':          # You choose Scissors
            points = 3 + 0
    elif a == 'B':              # Opponent chooses Paper
        if b == 'X':            # You choose rock
            points = 1 + 0
        elif b == 'Y':          # You choose Paper
            points = 2 + 3
        elif b == 'Z':          # You choose Scissors
            points = 3 + 6
    elif a == 'C':              # Opponent chooses Scissors
        if b == 'X':            # You choose rock
            points = 1 + 6
        elif b == 'Y':          # You choose Paper
            points = 2 + 0
        elif b == 'Z':          # You choose Scissors
            points = 3 + 3 
    return points

total_points = 0

with open('/Users/pettermartinussen/CS/Advent_of_Code_22/Day_2/input.txt','r') as f:
    for line in f:
        tekst = line
        a = tekst[0]
        b = tekst[2]
        total_points = total_points + check_points(a,b)

print('Total score: ' + str(total_points))