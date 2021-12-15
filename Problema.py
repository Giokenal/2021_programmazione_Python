#PROGRAMMA PER LA RISOLUZIONE DI UN PROBLEMA

# Un signore fa acquisti in 4 negozi diversi ed, in ognuno di essi, spende la metà di quanto
# ha all'entrata di ciascun negozio, più 7 euro. Alla fine gli rimangono 10 euro.
# Quanto ha speso in totale, ed in ciascun negozio?

# SOLUZIONE:

for x in range (0,100):
    if x-((x/2)+7)==10:
        for y in range (0,100):
            if y-((y/2)+7)==x:
                for z in range (0,1000):
                    if z-((z/2)+7)==y:
                        for a in range (0,1000):
                            if a-((a/2)+7)==z: 
                                risultato=(a-10)
                                print (a)   
                                print (z)
                                print (y)
                                print (x)
                                print (risultato)