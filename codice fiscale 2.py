import json
import pyfiglet
vocali='aeiouAEIOU'
mesi = { '01':'A','02':'B','03':'C','04':'D',
         '05':'E','06':'H','07':'L','08':'M',
         '09':'P','10':'R','11':'S','12':'T'}

c=input('Inserisci cognome: ')
n=input('Inserisci nome: ')
sesso=input('Inserire M o F: ' )
data=input('Inserisci data di nascita (gg/mm/aaaa): ').split('/')
comune=input('Inserisci comune di nascita: ').upper()

def main_screen():
    result=pyfiglet.figlet_format('Codice fiscale',font='slant')
    print(result)

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
        elif x=="'":
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
    for x in cons:
        if x==' ':
            cons.remove(x) 
            continue
        elif x=="'":
            cons.remove(x) 
            continue
    if len(cons)>3:
        cons[1:2]=[]
    risultato=''.join(cons+voc+['x']*2)[0:3]
    return risultato.upper()

def calcdata():
    anno=data[2][2:]
    mese=mesi[data[1]]
    if sesso=='M' or 'm':
        giorno=data[0]
    else:
        giorno=str(int(data[0])+40)
    risultato= anno+mese+giorno
    return risultato.upper()

def calccodcomune():
    codici=open('lista_comuni.txt','r')
    while 1:
        linea=codici.readline().strip()
        if not linea:
            codici.close()
            return 0
        com, codice=linea.split('\t')
        if com==comune:
            codici.close()
            return codice.upper()
main_screen()
print(calccognome()+calcnome()+calcdata()+calccodcomune())