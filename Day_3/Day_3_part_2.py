# Lag en funksjon som deler opp linjene i input
# Lag en funksjon som finner hvilken bokstav som er felles for de to individuelle tekststrengene
# Lag en funksjon som returnerer verdien til bokstaven

def del_linje(linje):
    lengde = len(linje)
    kutt = int(lengde/2)
    a = linje[0:kutt]
    b = linje[kutt:lengde]
    return a, b

def finn_felles(a, b):
    felles_bokst = []
    plass = 0

    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i] == b[j]:
                felles_bokst.append(a[i])
                plass = j
    felles_bokst = felles_bokst[0]
    return felles_bokst, plass       

def sjekk_verdi(bokstav):

    cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if bokstav.isupper():
        a, verdi = finn_felles(bokstav, cap)
        return verdi + 27
    else:
        a, verdi = finn_felles(bokstav,low)
        return verdi + 1

def finn_felles_badge(a,b,c):

    for x in range(len(a)):
        for y in range(len(b)):
            for z in range(len(c)):
                if a[x] == b[y] == c[z]:
                    return a[x]

sum = 0

with open('/Users/pettermartinussen/CS/Advent_of_Code_22/Day_3/input.txt') as f:
    for line in f:
        a,b = del_linje(line)
        bokstav, plass = finn_felles(a,b)
        verdi = sjekk_verdi(bokstav)
        sum = sum + verdi

#print(sum)

# Gå gjennom input tre linjer om gangen og finn felles item
# Finn verdien av item
# Sum opp

file = []

with open('/Users/pettermartinussen/CS/Advent_of_Code_22/Day_3/input.txt') as f:
    for line in f:
        tekst = line
        file.append(tekst.rstrip('\n'))

sum = 0

for x in range(0,len(file),3):
    a = file[x]
    b = file[x+1]
    c = file[x+2]
    felles = finn_felles_badge(a,b,c)
    verdi = sjekk_verdi(felles)
    sum = sum + verdi

print(sum)

