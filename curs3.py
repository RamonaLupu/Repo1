# structura alternativa if
# if fara indentare
a = 5
b = 10
# if a >b:
# print('a este mai mare decat b')

#if else
# if a > b:
#         print('a este mai mare decat b')
# else:
#         print('nu este mai mare')
#
# # elif
# if a < b:
#     print('a este mai mic decat b')
# elif a== b:
#     print('a egal cu b')
# else:
#     print('celelalte cazuri')
#
# # if cu operatori logici
# if a < b or a==b:
#     print('mesaj 1')
# else:
#     print('mesaj 2')

# exercitiul 4
'''
RO: Daca un client are peste 65 de ani, atunci va beneficia de o reducere de 15%.
Altfel, daca clientul nu are varsta de peste 65 de ani si calatoreste cu cel putin un copil, 
atunci acesta va beneficia de o reducere de 10%.
Pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 de ani) se va aplica
o reducere de 10% daca acestia calatoresc iarna.
De asemenea, pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta de 65) sau o taxa de manipulare de 1% altfel

'''

varsta = int( input('Va rugam sa introduceti varsta: '))
anotimp = str( input('va rugam sa introduceti anotimpul in care calatoriti: '))
clasa = int(input('introduceti clasa: '))
pretBilet = int(input('introduceti pretul biletului: '))

if varsta > 65:
    discount = 0.15
else:
    nrCopii = int(input('introduceti nr de copii care va insotesc: '))
    if nrCopii >= 1:
        discount = 0.1
if anotimp == 'iarna':
    discount += 0.1
if clasa == 1:
    taxa = 0.03
else:
    taxa = 0.01
pretBilet = pretBilet - pretBilet * discount + pretBilet * taxa
print(discount, taxa, pretBilet)

# scenariu: persoana peste 65 de ani care calatoreste iarna la clasa 1
# test case = cum testam?
# summary (test condition): verifica faptul ca pt un calator peste 65 ani, care calatoreste iarna, la clasa 1
# se aplica un discount de 25% si o taxa de 3%
#


