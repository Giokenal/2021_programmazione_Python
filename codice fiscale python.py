vocali='aeiouAEIOU '
c=input('Inserisci cognome')
# n=input('Inserisci nome')
# a=input('inserisci anno')
# mese=input('inserisci mese')

def calccognome():
    cons=[]
    voc=[]
    for x in c:
        if x in vocali:
            voc.append(x)
        else:
            cons.append(x)
    print ("".join(cons+voc+('x')*2)[0:3])

calccognome()


def prendiconsonanti():
    numero_caratteri=0
    risultato=''
    for lettera in c:
        if lettera not in vocali and numero_caratteri<3:
            risultato=risultato+lettera
            numero_caratteri=numero_caratteri+1
    return risultato.upper()
   
def prendivocali():
    numero_caratteri=0
    risultato=''
    if len(prendiconsonanti())<2:
        for lettera in c:
            if lettera in vocali and numero_caratteri<2:
                    risultato=risultato+lettera
                    numero_caratteri=numero_caratteri+1
        return risultato.upper()
    elif len(prendiconsonanti())<3:
        for lettera in c:
                if lettera in vocali and numero_caratteri<1:
                    risultato=risultato+lettera
                    numero_caratteri=numero_caratteri+1
        return risultato.upper()

def aggiungix():

    if len(prendiconsonanti()+prendivocali())<2:
        return (prendiconsonanti()+prendivocali())+'xx'.upper()
    elif len(prendiconsonanti()+prendivocali())<3:
        return (prendiconsonanti()+prendivocali())+'x'.upper()


def cognome():
    if len(prendiconsonanti())==3:
        return prendiconsonanti()
    elif len(prendiconsonanti()+prendivocali())==3:
        return (prendiconsonanti()+prendivocali())
    elif len(prendiconsonanti()+prendivocali())<3:
        return aggiungix()


def prendiconsonanti2():
    risultato=''
    for lettera in n:
        if lettera not in vocali:
            risultato=risultato+lettera
    return risultato[0:1].upper()+risultato[2:4].upper()
   

        
def prendivocali2():
    numero_caratteri=0
    risultato=''
    if len(prendiconsonanti2())<2:
        for lettera in n:
            if lettera in vocali and numero_caratteri<2:
                    risultato=risultato+lettera
                    numero_caratteri=numero_caratteri+1
        return risultato.upper()
    elif len(prendiconsonanti2())<3:
        for lettera in n:
                if lettera in vocali and numero_caratteri<1:
                    risultato=risultato+lettera
                    numero_caratteri=numero_caratteri+1
        return risultato.upper()

def aggiungix2():

    if len(prendiconsonanti2()+prendivocali2())<2:
        return (prendiconsonanti2()+prendivocali2())+'xx'.upper()
    elif len(prendiconsonanti2()+prendivocali2())<3:
        return (prendiconsonanti2()+prendivocali2())+'x'.upper()


def nome():
    if len(prendiconsonanti2())==3:
        return prendiconsonanti2()
    elif len(prendiconsonanti2()+prendivocali2())==3:
        return (prendiconsonanti2()+prendivocali2())
    elif len(prendiconsonanti2()+prendivocali2())<3:
        return aggiungix2() 

def anno():
    return (a[2:4])


codice_fiscale=cognome()+nome()+anno()
