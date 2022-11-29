# #    ex 1 for in for / parcurgerea unei matrici
# my_list = [
# 		[1,"test1"],
# 		[2,"test2", 3, "test3"],
# 		[34,"test4"],
# 		[5]
# ]
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(f'Valoare curenta a elementului din lista de pe pozitia[{i}][{j}] este: {my_list[i][j]}')
#
# #    ex 2  parcurgeti o lista de elemente, printati elem pe ecran si daca intalniti stringul 'gutui' inlocuitil cu caise
# list_2 = ['gutui', 'prune','mere', 'pere']
# for i in range(len(list_2)):
#     print(list_2[i])
#     if list_2[i] == 'gutui':
#         list_2[i] = 'caise'
# print(list_2)
#
# #   ex 3  Avem o lista de culori. Si vrem sa vindem haine in culorile respective
# # 			# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
# # 			# adica, daca cumparatorul ne spune ca nu ii place culoarea x, ii vom exclude de la prezentare hainele in culoarea respectiva
# culori_disponibile = ['rosu', 'albastru', 'roz', 'verde', 'galben', 'violet', 'magenta', 'maro']
# culori_nepotrivite_client = ['galben', 'albastru', 'maro']
# for culoare in range(len(culori_disponibile)):
#     if culori_disponibile[culoare] in culori_nepotrivite_client:
#         continue
#     print(f'Va recomandam haine in culoarea {culori_disponibile[culoare]}')
# print('________________')
# print('\n')
#
# culori_disponibile = ['rosu', 'roz', 'verde', 'galben', 'violet', 'magenta', 'maro''albastru']
# culori_nepotrivite_client = ['galben', 'albastru', 'maro']
# for culoare in range(len(culori_disponibile)):
#     if culori_disponibile[culoare] in culori_nepotrivite_client:
#         break
#     print(f'Va recomandam haine in culoarea {culori_disponibile[culoare]}')

#  for each
# parcurgem lista si daca intalnim soarece stergem
animale = ['cal', 'pisica', 'caine', 'magar', 'soarece', 'oaie', 'vaca']
# varianta cu for
# for animal in range(len(animale)-1):
#     if animale[animal] == 'soarece':
#         animale.pop(animal)
# print(animale)
# print('\n')
# varianta for each
# for animal in animale:
#     if animal == 'soarece':
#         animale.remove(animal)
# print(animale)
#
# # for else
# # printam toate nr pana la 5
# for i in range(6):
#     print(i)
# else:
#     print('Am terminat')
# print('\n')
# print('_____________')
# print('\n')
#
# # while
# i= 0
# while i <= 5:
#     print(i)
#     i = i+1
# else:
#     print('Am terminat')

#          Functii

# o modalitatea prin care putem sa econimisim cod

# 1. functii simple (fara parametri)
def print_noapte_buna():
    print('Noapte buna!')
    print('Este ora 8')

# print_noapte_buna()
# print_noapte_buna()
# print_noapte_buna()
# print_noapte_buna()
# print('\n')

# x = print_noapte_buna()
# print(x)
#
# def print_noapte_buna1():
#     print('Noapte buna!')
#     print('Este ora 8')
#     msg = 'sunt obosit'
#     return msg
# y = print_noapte_buna1()
# print(y)

# ex. suma a 2 nr
# calculeaza_suma() # functia tr mai intai definita si apoi apelata
# def calculeaza_suma():
#     a = 3
#     b = 4
#     suma = a + b
#     print(f'Suma celor 2 nr este {suma}')
#     return suma
#
# calculeaza_suma()
# x = calculeaza_suma()
# print(x)

# 2. functii cu parametri
# def suma(a,b):
#     sum = a + b
#     print(f' Suma celor 2 nr este: {sum}')
#     return sum
# suma(2,4)
#
#
# x = suma(3,5)
# print(x)

# functii cu nr indefinit de parametri
# facem o functie care calculeaza pretul unui bilet
# def calculeaza_pretul(*nr):
#     pret = 0
#     for element in nr:
#         pret += element
#     return pret
# print(calculeaza_pretul(2,6,7))
# print(calculeaza_pretul(1,3))
# print(calculeaza_pretul(2,6,7,1,3,2))

# Import date class from datetime module
from datetime import date
today = date.today()
print("Today date is: ", today)




