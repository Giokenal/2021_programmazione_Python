def indice():
    frutto=('banana')
    indice=0
    while indice<len(frutto):
        lettera=frutto[indice]
        print (lettera)
        indice=indice+1

indice()


def indice2():
    frutto=('banana')
    for lettera in frutto:
        print (lettera)

indice2()

def s():
    frutto='banana'
    print(frutto[0:4])

s()


parola='parola utente'
lettera=''
indice = 0
while(indice<len(parola)):
    if parola[indice]== lettera:
        print (indice)
    indice= indice+1

print (-1)