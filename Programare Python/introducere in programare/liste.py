# listele in python pot sa cuprinda elemente de tipuri diferite
# au dimensiune dinamica

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'
# afisam lista
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne da ultimul element
last = fructe.pop()
print('ultimul elem', last)
print('lista', fructe)

# de cate ori apare un element
print(fructe.count(3))

# extindem list
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)




