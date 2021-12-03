import json
from re import search
from typing import AnyStr
import dbfile
import pyfiglet


def main_screen():
    result = pyfiglet.figlet_format("Agenda", font="slant")
    print(result)

def main_menu():
    main_screen()
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
    ana['Nome']=input('Inserisci nome: ')
    ana['Cognome']=input('Inserisci cognome: ')
    ana['Telefono']=input('Inserisci numero di telefono: ')
    ana['Email']=input('Inserisci email: ')
    lista= dbfile.read_data()
    lista.append(ana)
    dbfile.save_data(lista)
    

def stampa():
    i=0
    lista=dbfile.read_data()
    print('Nome\t\tCognome\t\tTelefono\t\tEmail')
    for el in lista:
        print (el['Nome']+'\t'+el['Cognome']+'\t'+el['Telefono']+'\t\t'+el['Email'])
        i+=1
    return lista

    
def elimina():
    lst=stampa()
    id_lista=int(input('Selezionare ID da eliminare: '))
    del(lst[id_lista])
    dbfile.save_data(lst)
    return True
    

def ricerca():
    pass


