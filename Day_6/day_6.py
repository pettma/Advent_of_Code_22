# Lag en funksjon som tar inn en tekststreng
# Funksjonen blar gjennom tekststrengen bokstav for bokstav og sjekker tall opp mot hverandre i et intervall på fire og fire
# Hvis alle bokstavene i hvert intervall er ulike, returner plassen til den første verdien i intervallet

def finn_marker(tekst):
    
    for i in range(0,len(tekst)):
        intervall = []
        set_intervall = []
        a,b,c,d = tekst[i],tekst[i+1],tekst[i+2],tekst[i+3]
        intervall.append(a)
        intervall.append(b)
        intervall.append(c)
        intervall.append(d)
        for j in intervall:
            if j not in set_intervall:
                set_intervall.append(j)
        if intervall == set_intervall:
            return i+4
    return 'Error'

def finn_message(tekst):
    for i in range(0,len(tekst)):
        intervall = []
        set_intervall = []
        for j in range(i,i+14):
            intervall.append(tekst[j])
        for k in intervall:
            if k not in set_intervall:
                set_intervall.append(k)
        if intervall == set_intervall:
            print(intervall)
            print(set_intervall)
            return i+14
    return 'Error'


with open('/Users/pettermartinussen/CS/Advent_of_Code_22/Day_6/input.txt') as f:
    tekst = f.readline()
    print(finn_message(tekst))
