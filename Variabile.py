# variabila = zona din memorie care tine date
# variabila = cutiuta in care punem valori

# am declarat si initializat varialila marca
marca_masina = 'volvo'

model_masina = 'xc 60'

# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica
# loosely typed - nu tr sa specificam tipul de date
print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

# suprascriere
model_masina = 'xc 60 facelift'
print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

nume = 'Sinpetrean'
prenume = 'Andy'
varsta = '34'
print(nume + ' ' + prenume)
print(f'{nume} {prenume} si am varsta de {varsta}' )
