import json
import pyfiglet
#from termcolor import colored
import os

def inserisci():
    ana = {}
    ana['nome'] = input('Nome: ')
    ana['cognome'] = input('Cognome: ')
    ana['email'] = input('Email: ')
    ana['telefono'] = input('Telefono: ')
    lista = read_data()
    lista.append(ana)
    save_data(lista)

def stampa():
    lista = read_data()
    count = 0
    for el in lista:
        print(str(count),str(el))
        count += 1
    input("\n\nPress key to continue")
    return lista

def modifica():
    pass

def cancella():
    lst = stampa()
    id_del = int(input("Inserisci ID da cancellare: "))
    del(lst[id_del])
    save_data(lst)
    return True

def main_screen():
    result = pyfiglet.figlet_format("Agenda", font="slant")
    #print(colored(result,"red"))
    print(result)

def save_data(dt):
    fp = open('agenda.dat', 'w')
    fp.write(json.dumps(dt))
    fp.close()

def read_data():
    fp = open('agenda.dat', 'r')
    dati_agenda = fp.read()
    fp.close()
    return json.loads(dati_agenda)

def clear_dbfile():
    fp = open('agenda.dat', 'w')
    fp.write('[]')
    fp.close()

# menu gestione programma

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_screen()
    print("\n")
    print("1. Inserisci")
    print("2. Stampa")
    print("3. Modifica\n\n")
    print("10. Elimina\n\n")
    print("11. Purge DB\n")
    print("99. Esci\n\n")

    cmd = input("#: ")
    if(cmd == '99'):
        exit()
    elif(cmd=='1'):
        inserisci()
    elif (cmd == '2'):
        stampa()
    elif (cmd == '3'):
        inserisci()
    elif (cmd == '10'):
        cancella()
    elif (cmd == '11'):
        clear_dbfile()
    else:
        print("comando inserito: " + cmd)
    return True
