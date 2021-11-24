vocali='aeiou'
consonanti='bcdfghjklmnpqrstvxyz'
def cognome():
    c=input('inserisci cognome')
    result=''
    if consonanti in c<3:
        for lettera in range (len(c)):
                result=result+c[lettera]
        return result[0:3].upper()
    else:
        for lettera in range (len(c)):
            if c[lettera] not in vocali:
                result=result+c[lettera]
        return result[0:3].upper()

print(cognome())


# def nome():
#     n=input('inserisci nome')
#     result=''
#     nome = ''
#     for lettera in range (len(n)):
#         if n[lettera] not in vocali:
#             result=result+n[lettera]
#     result=result[0:1]+result[2:4]
#         # for i in range (len(result)):
#         #     if i==0:
#         #         nome=nome+result[i]
#         #     if i==2:
#         #         nome=nome+result[i]
#         #     if i==3:
#         #         nome=nome+result[i]
#         # return nome
#     return result.upper()

# def anno():
#     a=input('inserisci anno')
#     return a[2:4]
# def mese():
#     m=input('inserisci mese')
#     if m=='gennaio':
#         return'A'
#     elif m=='febbraio':
#         return'B'
#     elif m=='marzo':
#         return'C'
#     elif m=='aprile':
#         return'D'
#     elif m=='maggio':
#         return'E'
#     elif m=='giugno':
#         return'H'
#     elif m=='luglio':
#         return'L'
#     elif m=='agosto':
#         return'M'
#     elif m=='settembre':
#         return'P'
#     elif m=='ottobre':
#         return'R'
#     elif m=='novembre':
#         return'S'
#     elif m=='dicembre':
#         return'T'



# print (cognome()+nome()+anno()+mese())



