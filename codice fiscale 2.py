vocali='aeiouAEIOU'
c=input('Inserisci cognome')
n=input('Inserisci nome')
def calccognome():
    cons=[]
    voc=[]
    for x in c:
        if x in vocali:
            voc.append(x)
        else:
            cons.append(x)
        risultato=''.join(cons+voc+['x']*2)[0:3]
    return risultato.upper()

def calcnome():
    cons=[]
    voc=[]
    for x in c:
        if x in vocali:
            voc.append(x)
        else:
            cons.append(x)
        cons.remove([1:2])
        risultato=''.join(cons+voc+['x']*2)[0:3]
    return risultato.upper()

print(calcnome())