def main_menu():
    print('Benvenuto in agenda seleziona un menu per continuare')
    print('1) Inserisci')
    print('2) Elimina')
    print('3) Ricerca\n')
    print('4) Stampa\n\n')
    print('99) Esci')

    return int(input('# '))

def inserisci():
    ana={}
    print('Inserisci nuova anagrafica\n')
    ana['nome']=input('Inserisci nome: ')
    ana['cognome']=input('Inserisci cognome: ')
    ana['telefono']=input('Inserisci numero di telefono: ')
    ana['email']=input('Inserisci email: ')
    return ana
    
    
def elimina():

    pass

def ricerca():
    
    pass

def stampa(ana):
    print('Nome\t\tCognome\t\tTelefono\t\t\t\Email')
    for el in ana:
        print (el['nome']+'\t\t'+el['cognome']+'\t\t\t'+el['telefono']+'\t\t\t\'+el['email'])

    


