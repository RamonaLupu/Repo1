# #      1.
# def suma(a,b):
#     sum = a + b
#     print(f' Suma celor 2 nr este: {sum}')
#     return sum
# print(suma(18,95))
# print(suma(20,17))
#
# #      2.
# def functie_True_False(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# print(functie_True_False(5))
# print(functie_True_False(6))
import calendar

# #      3.
# def nr_caractere(nume, prenume, nume_mijlociu):
#     nrTotalDeCaractere = len(nume + prenume + nume_mijlociu)
#     return nrTotalDeCaractere
# print(nr_caractere('Lupu', 'Ramona', 'Catalina'))

# #      4.
# def arie_dreptunghi():
#     lungime = int(input(f'Lungimea dreptunghiului este: '))
#     latime = int(input(f'Latimea dreptunghiului este: '))
#     aria = lungime * latime
#     return f'Aria dreptunghiului este {aria}'
# print(arie_dreptunghi())


# #      5.
# def aria_cercului(r):
#     import math
#     aria = math.pi * r ** 2
#     return f'Aria cercului de raza {r} este {aria}'
# print(aria_cercului(5))
# print(aria_cercului(1))


#       6.
# def gaseste_x(x):
#     string_dat = 'balon'
#     if x in string_dat:
#         return (True)
#     else:
#         return (False)
# print(gaseste_x('o'))
# print(gaseste_x('r'))

#       7.
# def nr_de_caractere():
#     string = 'Vara asta am vizitat Parisul cu Dan.'
#     x = 0
#     y = 0
#     for i in string:
#         if i.islower():
#             x += 1
#         elif i.isupper():
#             y += 1
#     print(f'Nr de caractere lower case este {x}')
#     print(f'Nr de caractere upper case este {y}')
# print (nr_de_caractere())

# def nr_de_caractere(string):
#     x = 0
#     y = 0
#     for i in string:
#         if i.islower():
#             x += 1
#         if i.isupper():
#             y += 1
#     print(f'Nr de caractere lower case este {x}')
#     print(f'Nr de caractere upper case este {y}')
# print (nr_de_caractere('Vara asta am vizitat Parisul cu Dan'))
# nr_de_caractere('Numele lui este Alin.')


#       8.
# def lista_nr_pozitive(*lista):
#     nr_pozitive = []
#     for i in range(len(lista)):
#         if lista[i] > 0:
#             nr_pozitive.append(lista[i])
#             i += 1
#     return print(nr_pozitive)
# lista_nr_pozitive(2,-1,3,-2)
# lista_nr_pozitive(-5, 4, 2,-7, 8, 10, 11, -1, 1)
#
#
# lista_numere = [1, -4, 78, -5, 0, 85, 4, -10, -2]
# def numere_pozitive(numere):
#     lista_numere_pozitive = []
#     for numar in numere:
#         if numar > 0:
#             lista_numere_pozitive.append(numar)
#     return lista_numere_pozitive
# print(numere_pozitive(lista_numere))

#    9.
# def comparare(x,y):
#     if x > y:
#         print(f'Primul nr ({x}) este mai mare decat al doilea nr ({y})')
#     elif x < y:
#         print(f'Al doilea nr ({y}) este mai mare decat primul nr ({x})')
#     else:
#         print(f'Numerele sunt egale')
# comparare(4, 2)
# comparare (5, 9)
# comparare(2, 2)


#      10.
# def printeaza(a, set):
#     if a  in set:
#         print(f'Nu am adaugat nr in set. Acesta exista deja.')
#         return False
#     else:
#         set.add(a)
#         print(f'Am adaugat nr nou in set.')
#         return True
# print(printeaza(1, {6, 5, 8}))
# print(printeaza(1, {1,2,3}))


#    op. 1.
# def cate_zile_sunt_in_luna(luna):
#     import calendar
#     an = 2022
#     a = (calendar.monthrange( an, luna))
#     print(a[1])
# cate_zile_sunt_in_luna(2)
# cate_zile_sunt_in_luna(4)


# def calendar(luna):
#     lunile_anului = {
#         'January': 31,
#         'February': 28,
#         'March': 31,
#         'April': 30,
#         'May': 31,
#         'June': 30,
#         'July': 31,
#         'August': 31,
#         'September': 30,
#         'October': 31,
#         'November': 30,
#         'December': 31
#     }
#     if luna in lunile_anului:
#         return lunile_anului.get(luna)
#
#
# print(calendar('June'))
# print(calendar('January'))
# print(calendar('February'))



#    op. 2.
# def calculator(x,y):
#     a = x + y
#     b = x - y
#     c = x * y
#     d = x / y
#     return f'''
#     'Suma:', {a}
#     'Diferenta:', {b}
#     'Imnultirea:', {c}
#     'Impartirea:', {d}'''
#
#
# print(calculator(10,2))
# print(calculator(35,5))


#    op. 3.
# def returneaza_dict(*lista):
#     dict = {}
#     for i in lista:
#         dict[i]=lista.count(i)
#     return dict
# print(returneaza_dict(1,2,4,5,4,8,0,4,9,1,7,4))
# print(returneaza_dict(2,1,3,1,3,4))


#     op.4
# def nr_max(a,b,c):
#     x = max(a,b,c)
#     return x
# print(nr_max(2,5,1))
# print(nr_max(3,1,8))

# def maxim(x, y, z):
#     if x == y == z:
#         return ('numerele sunt egale')
#     elif x >= y and x >= z:
#         return (f'{x} este cel mai mare numar')
#     elif y >= x and y >= z:
#         return (f'{y} este cel mai mare numar')
#     else:
#         return (f'{z} este cel mai mare numar')
#
#
# print(maxim(20, 20, 2))
# print(maxim(5, 100, 100))
# print(maxim(7, 7, 7))
# print(maxim(17, 2, 17))


#     op. 5
# def suma_nr(a):
#     s = 0
#     for i in range(a+1):
#         s+=i
#     return s
# print(suma_nr(1))
# print(suma_nr(5))


#     bonus 1.
# def lista_nr_comune(lista1, lista2):
#     nr_comune = []
#     for i in lista1:
#         if i in lista2:
#             nr_comune.append(i)
#             return set(nr_comune)
#
# print(lista_nr_comune([1,1,2,3], [2,2,3,4]))


#   bonus 2.

    

























