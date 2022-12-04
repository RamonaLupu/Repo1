from abc import ABC, abstractmethod # avem nevoie de importurile acestea pentru abstractizare in python
# from functools import wraps
#
#
class Car(ABC): # Am definit clasa Car care mosteneste conceptul de abstractizare (fara mostenirea asta nu o putem face abstracta)

    @abstractmethod # am folosit un decorator ca sa marcam metoda ca abstracta
    def accelerate(self): # am inceput definirea metodei abstracte = metode fara corp (logica interna)
        # in general metodele abstracte nu trebuie sa aiba logica, si atunci pentru a nu avea erori avem doua optiuni:
        pass   # scriem pass
        # raise NotImplementedError - ridicam o exceptie de NotImplemented

    def stop(self): # O clasa abstracta poate sa contina si metode normale (care au logica interna)
        print("STOP!")  #  metodele de clasa, cu logica, nu este obligatoriu sa fie implementate in clasele mostenitoare
                                # decoratorul classmethod e optional, dar de regula il punem pentru claritate



#Aici am definit o clasa noua numita Ferrari care mosteneste clasa abstracta Car, ceea ce inseamna ca noi vom fi
                        #fortati sa implementam metoda abstracta accelerate

# def upper_case(func):
#     @wraps(func)
#     def func_wrapper(text):
#         return func().upper()
#     return func_wrapper
#
# @upper_case
# def accelerate(text):
#     print(text)

# accelerate()

class Ferrari(Car):
    culoare = None

    def accelerate(self):  # daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("test")  # puteti sa incercati sa o comentati sa vedeti ce se intampla

    def stop(self): # poly
        print("I'm a F, I can't stop")



# # Am implementat din nou o clasa care mosteneste clasa abstracta Car. Aici de asemenea suntem obligati sa implementam metoda accelerate
#
class Lastun(Car):
    def accelerate(self):
        print("I'm accelerating from 0 to 100 in 15 seconds")


f = Ferrari()
f.accelerate()
f.stop()

l = Lastun()
l.accelerate()
l.stop()

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         raise NotImplementedError
#     @abstractmethod
#     def sleep(self):
#         raise NotImplementedError
# class Dog(Animal):
#     def sound(self):
#         print('Ham Ham!')
#     def sleep(self):
#         print('zzzzzz')
# class Cat(Animal):
#     def sound(self):
#         print('Miau Miau!')
#     def sleep(self):
#         print('rrrr')
# pisi = Cat()
# pisi.sound()
# max = Dog()
# max.sleep()



class Animal(ABC): # ABC  =  Abstract Base Class

    # @abstractmethod  # decorator care marcheaza metoda ca fiind abstracta
    def sound(self):
        raise NotImplementedError

    #  pass = cuvant cheie care defineste faptul ca corpul metodei nu are o logica efectiva, dar este folosit pentru ca acea metoda
         # sa poata sa aiba un corp
    #  raise NotImplementedError = modalitate prin care putem sa fortam in mod explicit exceptia de not implemented

    @abstractmethod
    def sleep(self):
        pass


# Atunci cand o clasa mosteneste o alta clasa de tip interfata sau clasa abstracta, spunem ca o implementeaza

class Dog(Animal):

    def sound(self):
        print('Ham Ham!')

    def sleep(self):
        print('zzzzzzzzz')

    def describe(self):
        print('I have an owner')


class Cat(Animal):
    def sound(self):
        print('Miau Miau!')

    def sleep(self):
        print('prrrrr')

    def describe(self):
        print('I own a human')

azorel = Dog()
tom = Cat()
azorel.sleep()
azorel.sound()
azorel.describe()

tom.sleep()
tom.sound()
tom.describe()