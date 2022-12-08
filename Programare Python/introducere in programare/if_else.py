# Flow control - if else
# evalueaza conditii si bifurca codul in functie de rezultat

piesa_faina = False
print('pormin rodio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par printam acest lucru
# altfel printam impar
nr = 4
#ce inseamna nr par? se imparte la 2 si rest 0
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# # if, else if,else
# # cum ne saluta robotelul in functie de ora?
# # luam date de la tastatura
# # ne asiguram ca sunt transformate din string in int
# ora = int(input('introdu ora'))
# if ora < 0:
#     print('ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora<= 18:
#     print('buna ziua')
# elif ora<= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora mai mare decat 24')
# CTRL + /

# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea ==1:
    print('ati ales ro')
elif optiunea == 2:
    print('ati ales eng')
else:
    print('nu am identificat optiunea, mai incearca')