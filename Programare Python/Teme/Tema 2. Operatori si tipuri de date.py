# if else - evalueaza conditii si bifurca codul in functie de rezultat

# x=-1
# print(x>=0 and int(x)==x)
# # sau

# x = 6
# if x>=0:
#     print('x este un nr natural')
# else:
#     print('x nu este un nr natural')

# x = -6
# if x>0:
#     print('x este pozitiv')
# elif x==0:
#     print('x este neutru')
# else:
#     print('x este negativ')

# x = 3
# print(-2<x<13)
# # sau
# print(x>-2 and x<13)
# # sau

# x = 7
# if -2<x<13:
#     print('True - nr este cuprins intre -2 si 13')
# else:
#     print('False - nr nu este intre -2 si 13')
# # sau
# if (x>-2 and x<13):
#     print(True)
# else:
#     print(False)
# # sau
# if x<=-2:
#     print(False)
# elif x>=13:
#     print(False)
# else:
#     print(True)

# x, y = 7, 3
# if (x - y) < 5:
#     print (True)
# else:
#     print(False)

# x = 3
# if (not 5<x<27):
#     print('True - x nu este intre 5 si 27')
# else:
#     print('False - x este intre 5 si 27')

# x= input()
# y= input()
# if x == y:
#     print('x este egal cu y')
# elif x>y:
#     print('x este mai mare')
# else:
#     print('y este mai mare')

# x, y, z = 1, 2, 2
# if (x == y and y!=z) or (x == z and z!=y) or (y ==z and z!=x):
#     print('Triunghiul este isoscel')
# elif x==y and y==z:
#     print("Triunghiul este echilateral")
# else:
#     print('Triunghiul este oarecare')

# x = input()
# if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u':
#     print('x este vocala')
# else:
#     print('x nu este o vocala')
# for nota in range(3, 11,1):
#   if nota <=4 and nota > 0:
#     print(f'{nota} => F')
#   elif 4 < nota <=6:
#     print(f'{nota} => E')
#   elif 6< nota <= 7:
#     print(f'{nota} => D')
#   elif 7<nota <= 8:
#     print(f'{nota} => C')
#   elif 8<nota <= 9:
#     print(f'{nota} => B')
#   else:
#     print(f'{nota} => A')

# x = int(input())
# if x % 2 == 0:
#   print('x este un nr par')
# else:
#   print('x este un nr impar')

# x, y, z = input()
# if ((x > y or x == y) and y >= z):
#   print('x')
# elif (y >x and x >= z):
#   print('y')
# else:
#   print('z')

# x = int(input())
# y = int(input())
# z = int(input())
# if x + y + z == 180:
#   print('triunghiul este valid')
# else:
#   print('triunghiul nu este valid')

# text = 'Coral is either the stupidest animal or the smartest rock'
# text_nou = text[0:5] +text [-5: len(text)]
# print(text_nou)


# text = 'Coral is either the stupidest animal or the smartest rock'
# x = text.index('rock')
# print(x)
# print(text[slice(x)])

# x = input()
# assert x[0].casefold() == x[len(x)-1].casefold()

# x='a'
# y='b'
# assert x==y

# x = input()
# if x[0].casefold() == x[len(x)-1].casefold():
#     print(True)
# else:
#     print(False)


# nr = '0123456789'
# # afisam doar nr pare
# print(nr[slice(0,10, 2)])
# # afisam doar nr impare
# print(nr[slice(1, 10, 2)])

import random
while True:
    print("Rolling Dice...")
    x= int(input('Alege un nr:'))
    zar = random.randint(1,6)
    print(f"Valoarea zarului este: {zar} ")
    if x < zar:
        print(f'Ai pierdut. Ai ales un nr mai mic. Ai ales {x} dar zarul a fost {zar}')
    elif x > zar:
        print(f'Ai pierdut. Ai ales un nr mai mare. Ai ales {x} dar zarul a fost {zar}')
    else:
        print(f'Ai ghicit. Ai ales {x} si zarul a fost {zar}')
    repeat = input("Roll Dice again? 'y' for yes & 'n' for no: ")
    if repeat == 'n':
        break