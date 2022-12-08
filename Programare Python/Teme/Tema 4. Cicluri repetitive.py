# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in range(len(mașini)):
#     print(f'1.Masina mea preferata este { mașini[masina]}')

# print('__________________________________________')
#
# for masina in mașini:
#     print(f'2.Masina mea preferata este {masina}')
#
# print('__________________________________________')
#
# masina = 0
# while masina < (len(mașini)):
#     print(f'3.Masina mea preferata este {mașini[masina]}')
#     masina +=1

#        2
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in range(1, len(mașini)-1):
#     mașini[masina] =mașini[masina].upper()
#
# else:
#     print(mașini)


#        3
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in mașini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dvs.')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam.')

#        4
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in mașini:
#     if masina == 'Trabant' or masina == 'Lăstun':
#         continue
#     print(f'S-ar putea sa va placa masina {masina}')


#        5
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for masina in mașini:
#     if masina == 'Trabant':
#         masini_vechi.append(masina)
#         mașini[mașini.index(masina)] = 'Tesla'
#     if masina == 'Lăstun':
#         masini_vechi.append(masina)
#         mașini[mașini.index(masina)] = 'Tesla'
# print(f'Modele vechi: {masini_vechi}')
# print(f'Modele noi:{mașini}')


# #        6
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# for masina in pret_masini:
#     pret = pret_masini[masina]
#     if pret < 15000:
#         print(masina)
#
# for key, value in pret_masini.items():
#     if value <= (15000):
#         print(key, value)
#
# for key, value in pret_masini.items():
#     if value <= (15000):
#         print(f'Pentru un buget de 15000 euro puteti alege masina {key}')




# }
# for key, value in pret_masini.items():
#     if value <= (15000):
#         print(key, value)
# for key, value in pret_masini.items():
#         if value <= (15000):
#             print(f'Pentru un buget de sub 15000 euro puteti alege mașina', key)




#      7
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
# for i in numere:
#     if i==3:
#         x +=1
# print(f'Nr 3 apare de {x} ori.')


#      8
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
# for i in numere:
#     x +=i
# print(f'Suma numerelor este {x}')


#       9
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numere.sort()
# print(numere[-1])


#       10
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in numere:
#     if i > 0:
#        numere[numere.index(i)] = -i
# print(numere)




#    op. 1
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for i in alte_numere:
#     if i % 2 == 0:
#         numere_pare.append(i)
#     else:
#         numere_impare.append(i)
#     if i >= 0:
#         numere_pozitive.append(i)
#     else:
#         numere_negative.append(i)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)


#       op.2
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for i in range(len(alte_numere)-1, 0, -1):
#     for j in range(i):
#         if alte_numere[j]>alte_numere[j+1]:
#             t = alte_numere[j]
#             alte_numere[j] = alte_numere[j+1]
#             alte_numere[j+1] = t
# print(alte_numere)



#     op.3
# import random
# while True:
#     numar_secret = random.randint(1, 30)
#     x= int(input('User alege un nr:'))
#     if x < numar_secret:
#         print('Nr secret e mai mare.')
#     elif x > numar_secret:
#         print('Nr secret e mai mic.')
#     else:
#         print('Felicitari! Ai ghicit!')
#     break


#      op 4
x = int(input('Alege un numar:'))
for i in range(1, x+1):
    for n in range(i):
        print(i, end='')
    i +=1
    print('\n')






#    op.5

tastatura_telefon = [
                 [1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [0]
]
for i in tastatura_telefon:
    for j in i:
        print(f'Cifra curenta este', j)





