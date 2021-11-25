# lunghezzalista1=int(input('Inserire lunghezza lista'))
# lunghezzalista2=int(input('Inserire lunghezza lista'))
# lunghezzalista3=int(input('Inserire lunghezza lista'))
# lista1=[]
# lista2=[]
# lista3=[]
# for i in range (lunghezzalista1):
#     x=input('inserisci elemento: '+str(i)+':')
#     lista1.append(x)
# for i in range (lunghezzalista2):
#     x=input('inserisci elemento: '+str(i)+':')
#     lista2.append(x)
# for i in range (lunghezzalista3):
#     x=input('inserisci elemento: '+str(i)+':')
#     lista3.append(x)
# listafinale=[]
# listafinale.append(lista1)
# listafinale.append(lista2)
# listafinale.append(lista3)
# print (listafinale)

def multidimensional(list_element):
    nums=[]
    for i in range(3):
        nums.append([])
        for j in range(list_element):
            nums[i].append(2)
    return nums

print (multidimensional(3))