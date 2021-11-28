#ESERCIZIO 1

# n=0
# while n<10:
#     n=n+1
#     print(n)
# for n in range (0,10):
#     n=n+1
#     print (n)

#ESERCIZIO 2

# nome=input('Inserire nome: ')
# n=0
# while n<100:
#     print(nome)
#     n=n+1

#ESERCIZIO 3

# risultato=0
# n=int(input('Inserisci numero'))
# for n in range (0,n+1):
#      n=n+1
#      risultato=risultato+n
# print (risultato)

#ESERCIZIO 4

# n=int(input('Inserisci numero'))
# for i in range(1,11):
#     product=n*i
#         print (n)

#ESERCIZIO 5

# nome=input('Inserire nome: ')
# print (len(nome))

#ESERCIZIO 6

# nome=input('Inserire nome: ')
# print (nome.upper())
# print (nome.lower())

#ESERCIZIO 7

# nome=input('Inserire nome: ')
# risultato=''
# for n in range (len(nome)):
#     if n%2==0:
#         risultato=risultato+nome[n]
# print(risultato)

#ESERCIZIO 8
# nome=input('Inserire nome: ')
# ultimedue=nome[-2:]
# print(ultimedue*4)

#ESERCIZIO 9

# nome=input('Inserire nome: ')
# if len(nome)%4==0:
#     print (True)
# else:
#     print (False)

#ESERCIZIO 10

# nome=input('Inserire nome: ')

# print(sorted(sorted(nome),key=str.upper))

#ESERCIZIO 11

# nome=input('Inserire nome: ')
# c=input('Inserire carattere: ')

# if nome[0]==c:
#     print(True)
# else:
#     print (False)

#ESERCIZIO 12

# numero=float(input('Inserire numero float: '))
# print("\nOriginal Number: ", numero)
# print("Formatted Number: "+"{:.2f}".format(numero))

#ESERCIZIO 13

# numero=input('Inserire numero: ')
# print('0'*len(numero)+numero)
# OR
# numero=int(input('Inserire numero: '))
# result=''
# numeroinstringa=str(numero)
# for i in range(0,len(numeroinstringa)):
#     result=result+'0'
# print(result+numeroinstringa)

#ESERCIZIO 14

# def niente_e(stringa):
#     for lettera in stringa:
#         if lettera=='e':
#             return False
#         
#     return True

# print (niente_e('casa'))

# def niente_e(stringa,carattere_vietato):
#     for lettera in stringa:
#         if lettera==carattere_vietato:
#             return False

#     return True

# print (niente_e('casa','a'))
        
# ESERCIZIO 15,16,17

# n=int(input('Inserire numero: '))
# pari=[]
# dispari=[]
# for i in range (0,n):
#     if i%2==0:
#         pari.append(i)
#     else:
#         dispari.append(i)
# contatore = 0
# somma_pari = 0
# while(contatore<len(pari)): 
#     somma_pari = somma_pari + pari[contatore]
#     contatore += 1

# contatore = 0
# somma_dispari = 0
# while(contatore<len(dispari)): 
#     somma_dispari = somma_dispari + dispari[contatore]
#     contatore += 1

# print(somma_dispari)
# print(somma_pari)

# ESERCIZIO 18

# n=int(input('Inserire numero: '))
# lista=[]
# for i in range (0,n+1):
#     if i%2==0:
#         lista.append(i)
# for x in range (len(lista)):
#     print('Elemento in posizione'+str(x)+': '+str(lista[x]))

# ESERCIZIO 19

# lista=[]
# somma=0
# for i in range (0,10):
#     numero=int(input('Inserire numero: '))
#     lista.append(numero)

# for x in lista:
#     somma=somma+x
# print (lista)
# print (somma)
    
# ESERCIZIO 20

# l1=int(input('Inserire lunghezza lista: '))
# lista1=[]
# l2=int(input('Inserire lunghezza lista: '))
# lista2=[]
# lista_result=[]
# for i in range(0,l1):
#     s=input('Inserisci elemento'+str(i)+': ')
#     lista1.append(s)

# for i in range(0,l2):
#     s=input('Inserisci elemento'+str(i)+': ')
#     lista2.append(s)

# for elemento in lista1:
#     if elemento not in lista2:
#         lista_result.append(elemento)
# for elemento in lista2:
#     if elemento not in lista1:
#         lista_result.append(elemento)

# print (lista_result) 

# ESERCIZIO 21

# l1=int(input('Inserire lunghezza lista: '))
# lista=[]
# listafin=[]
# for i in range(0,l1):
#     s=input('Inserisci elemento'+str(i)+': ')
#     lista.append(s)
# n=int(input('Lunghezza minima: '))
# for elem in lista:
#     if len(elem)>n:
#         listafin.append(elem)
# print(listafin)

# ESERCIZIO 22

# l1=int(input('Inserire lunghezza lista: '))
# lista=[]
# for i in range(0,l1):
#      s=input('Inserisci elemento'+str(i)+': ')
#      lista.append(s)
#      stringa=''.join(lista)
# print (stringa)

# ESERCIZIO 23
# import random
# l1=int(input('Inserire lunghezza lista: '))
# lista=[]
# for i in range(0,l1):
#       s=input('Inserisci elemento'+str(i)+': ')
#       lista.append(s)
# print(random.sample(lista,1))

# ESERCIZIO 24

# def multidimensional(list_element):
#     nums=[]
#     for i in range(3):
#         nums.append([])
#         for j in range(list_element):
#             nums[i].append(0)
#     return nums

# print (multidimensional(3))

# ESERCIZIO 25

# def multidimensional(n):
#     nums=[]
#     for i in range(n):
#         nums.append([])
#         for j in range(1,n+1):
#             nums[i].append(j)
#     return nums

# print (multidimensional(3))

# ESERCIZIO 26

# t=('a','b','c')
# s=(input('Inserisci tupla'))
# print (t+(s,))


