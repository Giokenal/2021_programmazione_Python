# s=input('Inserisci stringa')
# print (s.upper())
# print (s.lower())

# s=input('Inserisci stringa')
# if s==s.upper():
#     print(s)
#     print(s.lower())
# else:
#     print(s.upper())
#     print(s.lower())

# s=input('Inserisci stringa')
# contatore=0
# while (contatore<len(s)):
#     c=s[contatore]
#     if contatore%2==0:
#         print (c.upper())
#     else:
#         print (c.lower())    
#     contatore=contatore+1

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

s=input('Inserisci stringa')
result=''
for lettera in range (len(s)):
    c=s[lettera]
    if is_even(lettera):
        result=result+s[lettera].upper()
        #print (c.upper())
    else:
        result=result+c.lower()
        #print (c.lower()) 
print (result)




