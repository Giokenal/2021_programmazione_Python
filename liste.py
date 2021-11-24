
lista1=[]
for i in range (0,4):
        x=input('inserisci elemento'+str(i)+':')
        lista1.append(x)
        

lista2=[]
for i in range (0,3):
        x=input('inserisci elemento'+str(i)+':')
        lista2.append(x)
        

# for x in lista2:
#     while x in lista1:
#         lista1.remove(x)

def diff():
    listaresult=[]
    for x in lista1:
        if x not in lista2:
            listaresult.append(x)
    for x in lista2:
        if x not in lista1:
            listaresult.append(x)
    return listaresult

print (diff())

    




