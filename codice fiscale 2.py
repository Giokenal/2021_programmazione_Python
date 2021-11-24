vocali='aeiouAEIOU'
mesi = { '01':'A','02':'B','03':'C','04':'D',
         '05':'E','06':'H','07':'L','08':'M',
         '09':'P','10':'R','11':'S','12':'T'}
c=input('Inserisci cognome')
n=input('Inserisci nome')
data=input('Inserisci data di nascita (gg/mm/aaaa): ').split('/')
def calccognome():
    cons=[]
    voc=[]
    for x in c:
        if x in vocali:
            voc.append(x)
        else:
            cons.append(x)
    for x in cons:
        if x==' ':
            cons.remove(x) 
            continue
    risultato=''.join(cons+voc+['x']*2)[0:3]
    return risultato.upper()

def calcnome():
    cons=[]
    voc=[]
    for x in n:
        if x in vocali:
            voc.append(x)
        else:
            cons.append(x)
    if len(cons)>3:
        cons[1:2]=[]
    risultato=''.join(cons+voc+['x']*2)[0:3]
    return risultato.upper()

def calcdata():
    anno=data[2][2:]
    mese=mesi[data[1]]
    risultato= anno+mese
    return risultato.upper()
print(calccognome()+calcnome()+calcdata())