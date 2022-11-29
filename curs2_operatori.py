# operatori de atribuire = , +=, -=, *=, /=

variabila1 = 7
variabila1 = 53
# +=
# variabila1 += 7
# print(variabila1)
variabila1 = variabila1 + 7
print(variabila1)

list1 = [1, 2, 3]
list2 = [4, 5]
print(id(list1),id(list2))
# list1+=list2
# print(list1)
print(id(list1))
list1 = list1 + list2
print(list1)
print(id(list1))

# operatorul -=
var2 = 47
var2 -= 7
print(var2)
var2 = var2-7
print(var2)

# operatorul *=
var2 = 7
var2 *= 7 # val anterioara se va inmulti cu 7 iar rezultatul final se va suprascrie in var2
print(var2)
var2 = var2*2
print(var2)

# /=
var2 = 7
var2 /= 7
print(type(var2))
var2 = var2/2
print(var2)

# operatori aritmetici +, - , *, /, **, %, //
nr1 = 2
nr2 = 3
print(f'Suma este  {nr1 + nr2}')
print(f'Diferenta este  {nr1 - nr2}')
print(f'Produsul este  {nr1 * nr2}')
print(f'impartirea este  {nr1 / nr2}')
print(f'Restul este  {nr1 % nr2}')
print(f'Rezultatul este  {nr1 // nr2}')
print(f'Ridicare la putere este  {nr1 ** nr2}')

# operatori de comparare ==, <=, >=, <, >, !=
# returneaza un rezultat de tip boolean
nr1 = 5
nr2 = 6
print(nr1 == nr2)
print(nr1 <= nr2)
print(nr1 >= nr2)
print(nr1 < nr2)
print(nr1 > nr2)
print(nr1 != nr2)

# operatori logici and, or, not
# ordimea prioritatilor not, and, or

nr1 = 5
nr2 = 6
print(nr1 > nr2 or nr1 == nr2) # False or False => False
print(nr1 > nr2 or nr1 < nr2) # False or True => True
print(nr1 > nr2 and nr1 < nr2) # False and True => False
print(not nr1 > nr2 and nr1 < nr2) # True and True => True
print(not(nr1 > nr2 and nr1 < nr2)) # not False = True
print(not nr1 == nr2 and not nr1 >= nr2) # not False and not false => true and True => True