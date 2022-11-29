import math

from curs6import import Test_case1, Test_case2, Test_case3

# import math se cauta dupa modului built_in math apelandu-se functia import

# functii
# functii cu nr indefinit de parametri
# facem o functie care calculeaza pretul unui bilet
# def calculeaza_pretul(*pret):
#     total = 0
#     for element in pret:
#         total += element
#     return total
# print(calculeaza_pretul(2,6,7))
# print(calculeaza_pretul(1,3))
# print(calculeaza_pretul(2,6,7,1,3,2))

#  Functii cu kwargs <=> ** nume_argument
# sunt folosite pt a parcurge dictionare si pt a opera cu ele
# ex.
apa = {
    'borsec': {
        'nume': 'borsec',
        'producator': 'borsec',
        'imbuteliere': 'sticla'
    },
    'dorna':{
        'nume':'dorna',
        'producator': 'dorna',
        'imbuteliere': 'peturi'
    }
}
# def actionare_elemente_dictionar(**kwargs):
#     for key,values in kwargs.items():
#         print(f'Detalii despre apa: {key}')
#         for key_in, values_in in values.items():
#             print(f'Apa {key} are {key_in} : {kwargs[key][key_in]}')
# print(actionare_elemente_dictionar(**apa))
# print(apa)
#
# def actionare_elemente_dictionar1(**param1):
#     for i,j in param1.items():
#         print(f'Detalii despre apa: {i}')
#         for key, value in j.items():
#             print(f'Apa {i} are {key} : {param1[i][key]}')
# actionare_elemente_dictionar1(**apa)


# POO = programare orientata pe obiect
# clasa = tipar
# obiectul = reprezentarea efectiva a clasei
# atributele = proprietatile
# metodele = functii
#Exemplu: Clasa masina
'''Cand definim o clasa ne gandim ce atribute poate sa aiba elementul
si ce actiuni poate sa faca
A. O masina de exemplu poate sa aiba urmatoarele PROPRIETATI (<=> ATRTIBUTE):
 - culoare
 - viteza
 - an_fabricatie
 - marca
 - model
 - capacitate_rezervor
 - tip_combustibil
 - tractiune
 - serie_sasiu
 - cutie_viteze
 - numar_inmatriculare
B. O masina poate sa faca urmatoarele ACTIUNI ( <=> METODE)
 - pornire de pe loc
 - oprire
 - accelerare
 - franare
 - consum_instant 
 - re
 '''
# definirea unei clase = se face cu keywordul class, nume si :
# constructor = agent responsabil cu ceearea obiectului
# cei mai uzuali constructori sunt: constructor implicit si constructor explicit
# definirea unui constructor __init__(), intre paranteze se vor explica atributele care vrem sa existe in mod obligatoriu la crearea obiectului
# daca nu avem nici un parametru, at toate atributele vor fi optionale
# elementul self = este un keyword, ne ajuta sa accesam elem definite in interiorul clasei (fie ele atribute sau metode)

# class Scoala:
#     # atribute
#     nume_director = None
#     nr_clase = 0
#     nr_elevi_clasa = 0
#
#     # metode
#     def calc_nr_total_elevi(self, nr_clase, nr_elevi_clasa):
#         nr_total_elevi = nr_elevi_clasa * nr_elevi_clasa
#         return nr_total_elevi
# # instantiem un obiect al clasei scoala care va primi in mod implicit atributele si metodele clasei scoala
# scoala_Bob = Scoala()
# # print(scoala_Bob.nume_director)
# scoala_Bob.nume_director = 'Ion Bob'
# # print(scoala_Bob.nume_director)
# nr_clase = int(input('Introduceti nr de clase pt scoala Bob: '))
# nr_elevi_clasa = int(input('Introduceti nr de elevi din fiecare clasa pt scoala Bob:'))
# print(f'Nr total de elevi este {scoala_Bob.calc_nr_total_elevi(nr_clase,nr_elevi_clasa)}')
#
# # am instantiat un nou obiect al clasei Scoala
# scoala_Popovici = Scoala()
# scoala_Popovici.nume_director = 'Andrei Popovici'

continut = math.pi
print(f' pi are valoarea{continut}')

continut2 = math.factorial(3)
print(f'factorial de 3 este{continut2}')


my_test_case1 = Test_case1()
my_test_case2 = Test_case2()
my_test_case3 = Test_case3('Test_case_nr_0003', 'The test case validates the disign and functionality of the OK buton.')

my_test_case1.printeaza_test_case1()
my_test_case2.printeaza_test_case()
my_test_case3.printeaza_test_case()
print(my_test_case3.retun_name())
print(my_test_case3.return_summery())

