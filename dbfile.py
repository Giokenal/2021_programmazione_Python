import json
from os import read

def save_data(dt):
    fp=open('agenda.dat','w')
    fp.write(json.dumps(dt))
    fp.close()    

def read_data():
    fp=open('agenda.dat','r')
    dati_agenda= fp.read()
    fp.close()
    return json.loads(dati_agenda)

def clear_dbfile():
    fp=open('agenda.dat','w')
    fp.write('[{}]')
    fp.close()

