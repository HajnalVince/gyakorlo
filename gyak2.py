"""
knev = input("Kérem a keresztneved: ")
vnev = input("Kérem a vezetékneved: ")

teljes_nev = knev + " " +  vnev

print("Üdvözöllek",teljes_nev)
 """ 
# VAGY

"""
knev = "Panda"
vnev = "Kungfu"

üdvözlet = f" Üdv kedves {knev} {vnev}"
"""



import random

random_szamok = []

for i in range(4):
    random_szamok.append(random.randint(0,20))
    
    
    
osszeg = 0

for szam in random_szamok:
    osszeg += szam
    
print(osszeg, random_szamok)



