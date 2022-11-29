
#   1
# lista_note = ['do','re', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# slicer_method = slice(None,None,-1)
# lista_noua = lista_note[slicer_method]
# print(lista_noua)
# lista_noua.reverse()
# print(lista_noua)

#   2
# note = ['do','re', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note.count('do'))


#   3
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# print(lista1 + lista2)
# lista1.extend(lista2)
# print(lista1)
# #
# lista1.sort()
# print(lista1)
# lista1.remove(0)
# print(lista1)


#   5
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# print(lista1 + lista2)
# if lista1 == []:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
#
#
# #   6
# # lista1 = [3, 1, 0, 2]
# # lista2 = [6, 5, 4]
# # lista1.extend(lista2)
# # print(lista1)
# lista1.clear()
# print(lista1)


# #   7
# # lista1 = [3, 1, 0, 2]
# # lista2 = [6, 5, 4]
# # lista1.extend(lista2)
# # print(lista1)
# # lista1.clear()
# # print(lista1)
# #
# # if lista1 == []:
# #     print('Lista este goala')
# # else:
# #     print('Lista nu este goala')
#
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista1 = lista1 + lista2
# print(lista1)
# if lista1 == []:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
#
# lista1.clear()
# print(lista1)
#
# if lista1 == []:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

#   8
# dict1 = {'Ana':8, 'Gigel':10, 'Dorel':5}
# for key  in dict1:
#     print(key)


# #   9
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# for key in dict1:
#     print(key, ' a luat nota ', dict1[key])
# #
# #    10
# dict1.update({'Dorel' : 6})
# # dict1['Dorel'] = 6
# print('Dorel a luat nota ', dict1['Dorel'])
#
# # #    11
# del dict1['Gigel']
# dict1['Ionica'] = 9
# print(dict1)
#
#
# #    12
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)
# #
# # #   13
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor saptamanii.')
# else:
#     print('Weekend nu este un subset al zilelor saptamanii.')
# #
# # #    14
# print(zile_sapt.difference(weekend))
#
# # 15
# print(zile_sapt.intersection(weekend))



# exercitii optionale

#      1
jucatori = ['Banel', 'Chirita', 'Mutu', 'Marica', 'Hagi']
schimbari_efectuate = int(input('Introdu nr de schimbari efectuate: '))
schimbari_max = 3
jucator_schimbat = input('Introdu numele jucatorului care va fi scos din teren: ')
schimbari_ramase = schimbari_max - schimbari_efectuate

if jucator_schimbat in jucatori:
    if schimbari_efectuate<schimbari_max:
        jucator_nou = input('Introdu numele jucatorului care va intra in teren: ')
        jucatori.remove(jucator_schimbat)
        jucatori.append(jucator_nou)
        schimbari_efectuate = schimbari_efectuate + 1
        schimbari_ramase = schimbari_max - schimbari_efectuate
        print(f'A intrat {jucator_nou}, a iesit {jucator_schimbat}, mai ai {schimbari_ramase} schimbari.')
    else:
        print('Nu mai ai mutari.')
else:
    print(f'Nu se poate efectua schimbarea deoarece jucatorul nu este in teren, mai ai {schimbari_ramase} schimbari.')

