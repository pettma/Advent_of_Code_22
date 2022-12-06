# Fra unput, separer startsposisjon men instruksjoner
# Lagre hver stack som hver sin liste
# Lag en funksjon som flytter bokser fra en stack til en annen

def separer_input():
    startsposisjon = []
    instruksjoner = []
    temp = []

    with open('/Users/pettermartinussen/CS/Advent_of_Code_22/Day_5/input.txt') as f:
        for line in f:
                temp.append(line)

        for i in range(0,9):
            startsposisjon.append(temp[i].strip('\n'))
        for i in range(10,511):
            instruksjoner.append(temp[i].strip('\n'))
    return startsposisjon, instruksjoner

def fra_stack_til_liste(stack):
    liste = [[1],[2],[3],[4],[5],[6],[7],[8]]
    
    for i in range(0,8):
        for j in range(0,37):
            for n in range(1,35,4):
                if j == n:
                    liste[i].append(stack[i][j])

    ny_liste = []

    for j in range(1,10):
        temp = []
        for i in range(0,8):
            if liste[i][j] != ' ':
                temp.append(liste[i][j])
        temp.reverse()
        ny_liste.append(temp)
        
    return ny_liste

def flytt_instruksjon(liste):
    instruksjoner = []

    for line in liste:
        temp = []

        for t in line.split():
            try:
                temp.append(int(t))
            except ValueError:
                pass
        instruksjoner.append(temp)

    return instruksjoner

def flytt(liste,instruksjoner):

    for i in range(len(instruksjoner)):
        antall = int(instruksjoner[i][0])
        fra = int(instruksjoner[i][1])-1
        til = int(instruksjoner[i][2])-1

        temp = liste[til]
        stacks = []
        for j in range(antall):
            element = liste[fra].pop(-1)
            stacks.append(element)
        
        stacks.reverse()
        for x in stacks:
            temp.append(x)
        liste[til] = temp
    return liste

a, b = separer_input()
a = fra_stack_til_liste(a)
b = flytt_instruksjon(b)
liste = flytt(a,b)
print(liste)



