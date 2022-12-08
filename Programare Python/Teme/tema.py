# # dalmatieni
# i=1
# for i in range (1,20,3):
#     print(f' {i}')

# nume = 'Popescu'
# prenume = 'Nicu'
# varsta = 32
# inaltime = 1.75
# prezent = True
#
# print(type(nume))
# print(type(varsta))
# print(type(inaltime))
# print(type(prezent))

# round(inaltime)
# inaltime = round(inaltime)
# print(inaltime)
# print(type(inaltime))
#
# print('Buna ziua! Numele meu este ' + nume + '.')
# print('Am varsta de ' + str (varsta) + ' si inaltimea de ' + str(inaltime) + '.')
# print(f'Daca sunt prezent, colegii vei vor confirma cu: {prezent}.')
# print(f'Adunand varsta cu inaltimea rezulta: {varsta+inaltime}.')
#
# numeClient = input('Numele clientului este: ' )
# prenumeClient = input("Prenumele este: ")
# print(f'Numele complet are {len(numeClient) + len(prenumeClient)} caractere')

# lungime = int(input())
# latime = int(input())
# print(f'Aria dreptunghiului este {lungime * latime}')

# s = 'Coral is either the stupidest animal or the smartest  rock'
# assert s.isnumeric()
# txt = input()
# x = len(txt)
# a = (x/2)
# b = int(a)
# print(txt[b])

# def isPalindrome(s):
# 	return s == s[::-1]
#
# s = "kayak"
# ans = isPalindrome(s)
#
# assert ans == s
#
#
# assert ans== s

# s = 'dad'
# assert s == s[::-1]
# # print('yes')
# assert s != s[::-1]
# print('no')



# print(input().split()[0:3])
#
# text = input()
# a1=text[0]
# print(a1)
# text = text[0] + text[1:-1].replace(a1, a1.upper()) + text[-1]
# print(text)

user = input()
parola = str(input())
print('Parola pt userul ' + user + ' este ' + str('*' * len(parola)) + ' si are ' + str(len(parola)) + ' caractere.')


# user = input('Type your username here')  # get the username info from the keyboard and save it into a variable
# password = input('Type your password here')  # get the password info from the keyboard and save it into a variable
# characters = int(len(password))  # find out the number of characters for the password
# password = '*' * characters  # replace each character by *
# print(f'The password for user {user} is {password} and has {characters} characters')  # print the desired string