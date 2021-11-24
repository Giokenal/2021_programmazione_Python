def stampa():
    n=int(input('inserisci numero'))

    for contatore in range(1,n):
        if contatore%2==0:
            print (contatore)
            

stampa()

def stampa2():
    n=int(input('inserisci numero'))
    contatore=1
    while contatore<n:
        if contatore%2==0:
            print (contatore)
        contatore=contatore+1
        

stampa2()
