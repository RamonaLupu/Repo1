def printGreeting():
    print('buna ziua! bine ati venit!')

def printGreetingByName(nume, prenume):
    print(f'buna ziua{nume} {prenume}')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
    return 3.14

# ex. daca persoana e majora, altfel false
def verificareMajor(varsta):
    if varsta >=18:
        return True
    else:
        return False


# zona de apelare
printGreeting()
printGreeting()
printGreetingByName(' Sinpetrean', 'Andy')
printGreetingByName(' Sinpetrean', 'Crina')
printGreetingByName(' Sinpetrean', 'Ares')
print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(17))

# se ia varsta utilizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('cont creat. bine ai venit in aplicatie')
else:
    print('nu ai varsta minima necesara (18) pt a paria')