# #3. tupluri - structuri de date imutabile
#
# # definire tuplu gol
# t = ()
# print(type(t))
# # definire tuplu populat
# t = ('mere', 'pere', 'nectarine', 'gutui', 'pere')
# print(t)
#
# # functii care se pot folosi cu tuplu
# # functia "index"
# print(t.index('nectarine'))
# # functia "count"
# print(t.count('pere'))
#
# # 4. Dictionare
# # elementele sunt de tip cheie - valoare
# # cheile tr sa fie unice
# # cheile servesc drept inlocuitor pt index
# # sunt oedonate
# # definirea unui dictionar gol
# d = {}
# print(type(d))
# # definirea unui dict populat
# d= {
#     'marca' : 'Audi',
#     'model' : 'TT',
#     'an_fabricatie' : 2010,
#     'norma_euro' : 'Euro4',
#     'combustibil' : 'Benzina',
#     'model' : 'TT'
# }
# print(d)
# # functii _ accesarea elementelor
# print(f' Numele masinii este {d["marca"]}')
# print(f'Modelul este {d["model"]}')
# # adaugam elemente
# d['nr_locuri'] = 5
# print(d)
# d.update({'nr_roti':5})
# print(d)

# ramona = {'centuri' : True}
# d.update(ramona)
# print(d)
# stergere unui element
# d.pop('norma_euro')
# print(d)
# # accesam key sau valori
# print(f'Valorile proprietatilor masinii mele sunt {d.values()}')
# print(f'Proprietatile masinii mele sunt {d.keys()}')
# accesare perechilor key- valoare
# print(f'Dictionarul este format din urmatoarele elemente: {d.items()}')

# dictionar imbricat =
# apa_plata = {
#     "borsec": {
#         "nume": "borsec",
#         "producator": "borsec",
#         "cantitate_vanzare": "500ml",
#         "impachetare": "baxuri"
#     },
#     "aqua carpatica": {
#         "nume": "aqua carpatica",
#         "cantitate_vanzare": "2l",
#         "impachetare": "sticla"
#     },
#     "dorna":
#         {
#             "nume": "dorna",
#             "producator": "dorna",
#             "impachetare": "bax",
#             "promovare": {"reclama": "Hai gata cu fotosinteza, la culcare toata lulumea"},
#             "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
#         }
# }
# print(apa_plata['aqua carpatica']['impachetare'])
# print(apa_plata['dorna']['promovare']['reclama'])


# Structuti repetitive
# while
# for
# forich

# 1. str repetitiva while
# executam o serie de instructiuni atata timp cat o conditie este adevarata
# elementul sau variabila de control se declara , de regula, in afara while-ului
# ex. printati toate nr de la 1 la10
# i = 1
# while i <=10:
#     print(f'Nr curent este {i}')
#     i = i+1
  # printam 101 dalmatieni
# dalmatieni = 1
# while dalmatieni <= 101:
#     print(f'Dalmatianul curent are nr {dalmatieni}')
#     dalmatieni+=1
# printam suma nr de la 1 la 10
i = 0
suma = 0
while i<= 10:
    suma = suma + i
    i= i+1
print(suma)

# parcurgeti o lista si printati fiecare element
l1 = ['Ramona', 'Dan','Alex', 'Iulia', 'Carmen', 'Raul', 'Ramona2', 'Simona', 'Silviu']
i = 0
while i < len(l1):
    print(l1[i])
    i+=1
# inlocuim pe Silviu cu Adela
i=0
while i< len(l1):
    if l1[i] == 'Silviu':
        l1[i] = 'Adela'
    i +=1
print(l1)

# inlocuim Alex
i=0
while i< len(l1):
    if l1[i] == 'Alex':
        l1[i] = 'Andreea'
        break
    i +=1
print(l1)

# 2.for
# este utilizata atunci cand vrem sa parcurgem o lista cu scopul de a printa sau modifica elementele
# o mai utilizam atunci cand vrem sa executam un set de un nr specific de ori

# str unui For loop
# parcurgem nr la la 1 la 10 si printati le pe cele pare

# for i in range(0,11):
#     # capatul superior la range nu este luat in considerare
#     # start range are val 0 si poate fi omosa
#     if i%2 == 0:
#         print(i)
#     else:
#
# for i in range(11):
#     if i%2 != 0:
#         print(i)
#     else:
#         print('nu este impar')

for i in range(11):
    print(i)
    if i == 5:
        break

