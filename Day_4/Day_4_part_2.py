# Del opp fillinja i to
# Finn ut hvilke tall hver del omfatter
# Sjekk om disse overlapper med det andre paret
# Hvis alle overlapper legg til i svarsum

def del_opp(streng):                    # Returnerer en liste med de to strengene
    return streng.split(',')

def finn_tallrekke(liste):
    tallrekke = []
    start = int(liste[0])
    slutt = int(liste[1])+1
    for i in range(start,slutt):
        tallrekke.append(i)
    return tallrekke

def finn_intervall(liste):
    a = liste[0].split('-')
    b = liste[1].split('-')
    return finn_tallrekke(a),finn_tallrekke(b)

def sjekk_overlapp(a,b):
    if len(b) > len(a):
        temp = b
        b = a
        a = temp

    try:
        if a.index(b[0]) != -1:
            start = a.index(b[0])
            slutt = start + len(b)
            if a[start:slutt] == b:
                return True
    except:
        return False

def sjekk_delvis_overlapp(a,b):
    for i in a:
        for j in b:
            if i == j:
                return True
    return False

def finn_totalt_overlapp(line):
    line = del_opp(line)
    a,b = finn_intervall(line)
    sjekk = sjekk_delvis_overlapp(a,b)
    return sjekk

sum = 0

with open('/Users/pettermartinussen/CS/Advent_of_Code_22/Day_4/input.txt') as f:
    for line in f:
        print(line)
        if finn_totalt_overlapp(line) == True:
            sum += 1

print(sum)
