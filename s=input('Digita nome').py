s=input('Digita nome')
if len(s)>2: 
    penultimo=s[-2]
    ultimo=s[-1]
    var=4
print ((penultimo+ultimo)*var)

s=input('Digita nome')
while len(s)<2:
    s=input('Digita nome')
a=s[-2]
b=s[-1]
c=a+b
i=0
while i<3:
    c=c+a+b
    i=i+1
print (c) 


s=input('inserisci stringa')
while len(s)<2:
    s=input('inserisci stringa')
print(s[len(s)-2: ]*4)