# 1. Lista
# se defineste cu paranteze patrate []
# este o colectie de date ordonate, cu tipuri de date diferite sau de acelasi fel
# are poprietatea de a fi mutabila
# actiuni asupa unei liste:
# - adaugam elemente
# - stergem elemente
# - modificam un element de la un anumit index
# - sa mutam un element la un anumit index

# 1. deglararea si indexarea unei liste goale
a = []
# 2. declararea si initializarea unei liste populate
a_prezenti =['Raul', 'Simona', 'Alex', 'Dan', 'Ramona1']
a_absenti = ['Silviu', 'Carmen', 'Iulia', 'Ramona']
string_a = 'Ana are mere si este fericita'
a_split = string_a.split()
print(a_split)
# # 3. accesare elemente
# print(f'Primul element din lista este: {a_prezenti[0]}')
# print(f'Primul element din lista este: {a_absenti[0]}')
# # accesare ultimului element din lista
# print(f'Ultimul element din lista este: {a_prezenti[len(a_absenti)-1]}')
# print(f'Ultimul element din lista este: {a_prezenti[-1]}')
# # functia append
# a_prezenti.append('Adela')
# print(a_prezenti)
# # functia insert
# a_absenti.insert(2, 'Adela')
# print(a_absenti)
# # functia index
# print(a_absenti.index('Iulia'))
# functia remove
# print(a_prezenti.remove('Dan'))
# print(a_prezenti)
# functia pop
print(a_absenti.pop(-1))
print(a_absenti)
# functia count = de cate ori apare un element din lista
print(a_prezenti.count('Simona'))
print(a_prezenti.extend(a_absenti))
print(a_prezenti)
# a_prezenti.sort()
# ASCII:https://infoas.ro/lectie/90/codul-ascii-tabel-complet
# liste neomogene
# lista_neomogena = ['maria', 12, True, 15.3]


# 2. Seturi
# - structuri/colectii neordonate, imutabile (nu putem modifica valorile lor)
# - definire cu o pereche de acolade {}
# - operatii: accesare de elemente, adaugare elemente, stergere elemente

# # definirea unui set gol
# set_gol = set()
# print(type(set_gol))
# # definirea unui set populat
# set_populat = {'Caine', 'Pisica', 'Hamster', 'Papagal'}
# # accesarea unui element din set - varianta cu operatorul IN
# print('Hamster' in set_populat)
# assert 'Hamster' in set_populat, 'Error: hamster nu este in lista '
# # assert 'Gaina' in set_populat, 'Error: hamster nu este in lista '
#
# # functia add
# set_populat.add('Gaina')
# print(set_populat)
#
# # functia pop
# # set_populat.pop()
# # print(set_populat)
#
# # functia remove - da eroare daca elementul nu exista
# set_populat.remove('Hamster')
# print(set_populat)
#
# # functia discard - se executa dar fara sa returneze  eroare daca elementul nu exista
# set_populat.discard('Pisica')
# print(set_populat)

# functia update, union, clear,
# concatenare (doar se modifica lista noastra), union (se creeaza o a 3 lista care reprezinta concatenarea celor 2 implicate)

# tupluri si dictionare




