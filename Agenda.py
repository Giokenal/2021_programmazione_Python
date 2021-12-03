import Agendamenu as am
import json
import dbfile
import pyfiglet

rubrica={}
agenda=[]
item=0
while (item !=99):
    item=am.main_menu()
    if (item==1):
        new_ana=am.inserisci()
        agenda.append(new_ana)
        print(agenda)
    elif (item==2):
        am.elimina()
    
    elif (item==3):
        am.ricerca()

    elif (item==4):
        am.stampa()
    else:
        print ('Menu selezionato inesistente')
