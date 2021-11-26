# Esercizio 1

# In input una serie di numeri, li mette in una lista e poi li ordinate, 
# Una volta ordinate la stampate.(Senza usare il comando sort)
# blog.finxter.com/wp-content/uploads/2020/04/Python-List-Methods-Cheat-Sheet.pdf


# l1=int(input('Inserire lunghezza lista: '))
# lista=[]
# listaordinata=[]
# for i in range(0,l1):
#   n=int(input('Inserisci elemento '+str(i)+': '))
#   lista.append(n)
# while len(lista)>0:
#     listaordinata.append(min(lista))
#     lista.remove(min(lista))

# print(listaordinata)

import random
l1=int(input('Inserire lunghezza lista: '))
lista=[]
listaordinata=[]
for i in range(0,l1):
        n=random.randrange(0,100)
        lista.append(n)
while len(lista)>0:
        listaordinata.append(min(lista))
        lista.remove(min(lista))

print(listaordinata)