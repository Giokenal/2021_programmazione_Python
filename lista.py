lunghezzalista=int(input('Inserisci lunghezza lista'))
lista=[]
for i in range (lunghezzalista):
        x=input('inserisci elemento'+str(i)+':')
        lista.append(x)

n=int(input('Inserire numero base'))

contatore=0
for x in lista:
    if len(x[0])<n:
        lista.remove(x)
    else:
        
        contatore=contatore+1
    
    
    
    
print(lista)

# listaresult=[]
# for x in lista:
#     if len(x)>n:
#         listaresult.append(x)
# print(listaresult)

# lunghezzalista=int(input('Inserisci lunghezza lista'))
# lista=[]
# for i in range (lunghezzalista):
#         x=input('inserisci elemento'+str(i)+': ')
#         lista.append(x)

# for x in lista:
#     risultato=''.join(lista)
# print (lista)
# print (risultato.capitalize())
