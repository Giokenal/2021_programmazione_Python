# n=input('Inserisci parola')
# def niente_e():
#     for lettera in n:
#         if lettera =='e':
#             return False
#     return True

# print(niente_e())


# def numeri_pari(n):
#     pari=[]
#     for i in range(0,n+1):
#         if i%2==0:
#             pari.append(i)



# n=int(input('inserisci un numero'))
# pari=[]
# for i in range(0,n+1):
#     if i%2==0:
#         pari.append(i)
    
# contatore=0
# for numero_pari in pari:
#     contatore=contatore+1
#     print ('elemento in posizione '+str(contatore-1)+":"+str(numero_pari))

# lista_pari=numeri_pari(10)

# def indice():
#     pari=[]
#     contatore=0
#     for numero in lista_pari:
#         pari.append(numero)
#         contatore=contatore+1
#         pari.append(contatore)
#     print (pari)
# indice()


lista=[]

for x in range (0,3):
    x=int(input('inserisci numero'))
    lista.append(x)    
print (lista)

risultato=0
contatore=0
while contatore<len(lista):
    contatore=contatore+1
    risultato=risultato+x
print(risultato)



