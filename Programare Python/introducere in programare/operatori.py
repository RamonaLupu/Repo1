'''
Opertori
aritmetici: +,-,*,/, %
de comparare: <>, ==, !=, <=, >=
logici: and, or, !
'''

a = 3
b = 5
print(a+b) # 3+5 => 8
print(a==b) # 3=5 => False
print(a<b and a<4) # 3<5 si 3<4 => true si true => True

# cu mama sau tata sau (cu bunica si bunicul)
mama = True
tata = True
bunica = False
bunicul = False
print(mama or tata or (bunica and bunicul))