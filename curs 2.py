


poezie = 'Ana are mere si, este vesela pt ca este miercuri'
# extrage toate caracterele de la inceput pana la final cu specificarea pozitiei de start si de stop
# pozitia de start 0
# pozitia de stop len (poezie) = lungimea stringului
print (poezie[0:len(poezie)])
# extrage toate caracterele de la inceput pana la final cu specificarea pozitiei de start si de stop defauld
print(poezie[:])
# extrage toate caracterele de la inceput pana la final cu specificarea pozitiei de start si de stop si de pass
print(poezie[::])
# extragem toate caracterele de la inceput pana la final cu passul 2
print(poezie[0:len(poezie):2])
# extragem toate caracterele de la inceput pana la final cu passul 2
print(poezie[::2])
#  extragem toate caracterele de la poz 5 pana la pozitia 13 inclusiv
print(poezie[5:14])
# estragem ultimele 3 caractere de la final
print(poezie[len(poezie)-3:len(poezie)])
#vsau
print(poezie[-3:])
# printam stringul in ordine inversa
print(poezie[::-1])
# vrem sa impartim springul cu metoda 'split'pri = se returneaza o lista de elemente iar splitul se face dupa
print(poezie.split(sep=','))
print(poezie.split(sep='l'))
print(poezie.split(sep=' '))

# metoda replace
print(poezie.replace('A', 'm'))
print(poezie.replace('Ana', 'Maria'))

# metoda upper()
print(poezie.upper())
print(poezie.upper().replace('A', 'm'))

# metoda index () si find ()
print(poezie.index('A'))
print(poezie.index('a'))
print(poezie.find('a'))
''' dif dintre find si index este ca find returneaza -1 in care caracterul nu este gasit iar index ne retueneaza o eroare'''

# print(poezie.find('x'))
# print(poezie.index('x'))

# metosa isnumeric(), metoda count(), metoda capitalize()
numeric = '1234'
print(poezie.isnumeric())
print(numeric.isnumeric())
print(poezie.count('A'))
print(poezie.count('a'))

print(poezie.capitalize())