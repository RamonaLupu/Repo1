# Pilonii OOP
# mostenirea
# encapsularea
# polimorfismul
# abstractizarea

# # Mostenirea
# # avem 3 tipuri:  unica, pe mai multe niveluri, multipla (nu e ok sa o utilizam)
# class Chef(): # clasa parinte
#     cutite = None
#     linguri = None
#     def __init__(self, nr_cutite): # constructor cu parametru nr  cutite
#         self.cutite = nr_cutite
#     def make_salad(self): # metoda care printeaza
#         print('salad')
#     def make_fries(self):
#         print('fries')
# class Chef2(): # clasa parinte
#     sort = 2
# class JapaneseChef(Chef): # clasa copil care mosteneste din clasa parinte Chef(atribute si metode)
#     def __init__(self, cantitate_alge, cutite):  # constructor cu 2 parametri
#         self.alge = cantitate_alge
#         self.cutite = cutite
#     # metode
#     def make_sushi(self):  # metode
#         print('sushi')
# class ItalianChef(Chef, Chef2): # clasa copil care mosteneste din clasele Chef si Chef2  // mostenire multipla
#     tava = 1  # atribut propriu
#     def make_pizza(self): # metoda proprie
#         print('pizza')
#
#
# new_chef = Chef(4)  # instantiem un obiect de tipul clasei parinte Chef
# new_chef.make_fries()  # aplicam metoda make_fries
#
# japan_chef = JapaneseChef(10, 5)  # un nou obiect de tip JaponesChef
# # vrem sa modificam valorea atributului linguri din clasa parinte
# japan_chef.linguri = 6
# print(japan_chef.linguri)
# japan_chef.make_sushi()
# japan_chef.make_salad()
# mario_chef = ItalianChef(3) # metoda diamantului > daca am avea mai multi parametri(in ambele clase parinte)
# print(mario_chef.tava) # avem acces la atributul tava din clasa italianChef
# print(mario_chef.sort)
# print(mario_chef.linguri)
# mario_chef.linguri = 15 # suprascriem
# print(mario_chef.linguri)
#
# class Tokyo_Chef(JapaneseChef): # mostenire pe niveluri
#     alge = 300
#
# san_chef = Tokyo_Chef(150, 7)    # instantiem un obiect (parametrii sunt din clasa japanesechef
# # accesam o metoda din clasa parinte chef
# san_chef.make_salad()
#
#
# # un alt exemplu
# class Animal():
#     sunet = None
#     culoare = None
#     specie = None
#     varsta = 0
#     sunet_somn_mancare = None
#     def dorm(self):
#         print(f'Acum dorm {self.sunet_somn_mancare}')
#     def imbatranire(self):
#         self.varsta +=1
#         print(f'Acum am varsta de {self.varsta}.')
# class Pisica(Animal):
#     toarce = 'Da'
#     vaneaza_soareci = None
#     def toarce_sa_ceri_mancare(self):
#         if self. toarce == 'Da':
#             self.sunet_somn_mancare = 'Miau'
#             print(self.sunet_somn_mancare) # atribut al clasei Pisica
#
# # instantiem un obiect de tip animale
# pisica = Animal()
# # instantiem un obiect al clasei Pisica
# pisica_mostenitoare = Pisica()
# pisica.sunet = 'meow, meow'
# print(pisica.sunet)
# print(pisica_mostenitoare.sunet)
# pisica.dorm()
# pisica_mostenitoare.dorm()
# pisica.imbatranire()
# pisica_mostenitoare.imbatranire()

# Polimorfism
# polimorfism cu nr indefinit de parametri
print(len('abc'))
print(len([1,2,3,4]))

def suma_nr(*args):
    sum = 0
    for elem in args:
        sum += elem
    return sum
print(suma_nr(1,2))
print(suma_nr(4,6,9))
print(suma_nr(10,6,9,8))

# parametri initializati cu valoare default
def add (x, y = 0, z = 0): #  functie polimorfica
    return x + y + z
print(add(3,7,1))
print(add(3,1))
print(add(3))

# polimorfism prin implementarea aceleasi metode in  clase diferite
class America:
    limba = 'engleza'
    imn = 'imnul americii'
    drapel = 'drapel american'
    def printeaza_limba(self):
        print(f'Limba care se vorbeste in america va fi {self.limba}')
class Romania:
    limba = 'romana'
    imn = 'desteapta-te romane'
    drapel = 'tricolor'
    def printeaza_limba(self):
        print(f'Limba se vorbeste in Romania este {self.limba}')
america1 = America()
romania1 = Romania()
america1.printeaza_limba()
romania1.printeaza_limba()

# polimorfism
class Pasare:
    def discribe(self):
        print('sunt o pasare')
    def zboara(self):
        print('sunt o pasare deci zbor')
class Papagal(Pasare):
    def vorbeste(self):
        print('sunt o pasare si vorbesc deci sunt un papagal')
class Pinguin(Pasare):
    def zboara(self):
        print('nu pot zbura dar sunt frumos')
pasare1 = Pasare()
pasare1.zboara()
pasare1.discribe()
print('****')
papagal1 = Papagal()
papagal1.discribe()
papagal1.zboara()
papagal1.vorbeste()
print('***')
pinguin1 = Pinguin()
pinguin1.discribe()
pinguin1.zboara()

# encapsulare # ascunderea unor atribute/metode  sau restrictionarea lor
# abstractizarea = fara corp




