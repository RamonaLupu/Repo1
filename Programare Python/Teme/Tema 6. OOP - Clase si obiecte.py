# import math
# class Cerc:
#     raza = 0
#     culoare = None
#     def descrie_cerc(raza,culoare):
#         print(f'Cercul are culoarea {culoare} si raza = {raza}.')
#     def aria(raza):
#         import math
#         a = math.pi * raza ** 2
#         return f'Aria cercului este {a}.'
#
#     def diametru(raza):
#         d = 2 * raza
#         return print(f'Diametrul cercului este {d}.')
#
#     def circumferinta(raza):
#         d = 2 * raza
#         c = math.pi * d
#         return print(f'Circumferinta cercului este {c}.')
#
# cerc1 = Cerc
# cerc1.descrie_cerc(2,'roz')
# print(cerc1.aria(2))
# cerc1.diametru(2)
# cerc1.circumferinta(2)
#
# cerc2 = Cerc
# cerc1.descrie_cerc(5,'albastru')
# print(cerc2.aria(5))
# cerc2.diametru(5)
# cerc2.circumferinta(5)



#          2.
# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#     def descrie(self):
#         print(f'Dreptungiul are lungimea: {self.lungime}, latimea: {self.latime} si culoarea: {self.culoare}.')
#     def aria(self):
#         a = self.lungime * self.latime
#         return print(f'Aria dreptunghiului este: {a}.')
#     def perimetru(self):
#         p = 2 * (self.lungime + self.latime)
#         return print(f'Perimetrul dreptunghiului este: {p}')
#     def schimba_culoarea(self):
#         self.culoare = 'alb'
#
#
# dreptunghi1 = Dreptunghi(2, 4, 'galben')
# dreptunghi2 = Dreptunghi(1,6, 'mov')
# dreptunghi1.descrie()
# dreptunghi1.aria()
# dreptunghi1.perimetru()
# dreptunghi1.schimba_culoarea()
# dreptunghi1.descrie()
# print('\n')
# dreptunghi2.descrie()
# dreptunghi2.aria()
# dreptunghi2.perimetru()
# dreptunghi2.schimba_culoarea()
# dreptunghi2.descrie()


#         3.
# class Angajat:
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#     def descrie(self):
#         print(f'Angajatul cu numele: {self.nume} {self.prenume} are salariul: {self.salariu} RON.')
#     def nume_complet(self):
#         nume_angajat = self.nume + ' ' + self.prenume
#         return print(f'Numele complet al angajatului este: {nume_angajat}.')
#     def salariu_lunar(self):
#         salariu_net = int(self.salariu - (41.5 / 100 * self.salariu))
#         return print(f'Acesta are un salariu lunar net in valoare de: {salariu_net} RON ')
#     def salariu_anual(self):
#         salariu_an = 12 * self.salariu
#         return print(f'si un salariu anual de: {salariu_an} RON.')
#     def marire_salariu(self):
#         marire = 500
#         procent_marire = round ((marire / self.salariu * 100),2)
#         return print(f'Incepand de anul viitor va avea o marire salariala de {marire} RON, reprezentand un procent de {procent_marire}% din salariul actual.')
#
# angajat1 = Angajat ('Paiu', 'Ion', 4500)
# angajat1.descrie()
# angajat1.nume_complet()
# angajat1.salariu_lunar()
# angajat1.salariu_anual()
# angajat1.marire_salariu()
#
# print('\n')
#
# angajat2 = Angajat ('Maia', 'Ana', 5200)
# angajat2.descrie()
# angajat2.nume_complet()
# angajat2.salariu_lunar()
# angajat2.salariu_anual()
# angajat2.marire_salariu()



#     4.
# class Cont:
#     def __init__(self, iBan, titular, sold):
#         self.iBan = iBan
#         self.titular = titular
#         self.sold = sold
#     def afisare_sold(self):
#         print(f'Titularul, {self.titular}, are in contul {self.iBan} suma de {self.sold} RON.')
#     def debitare_cont(self):
#         suma_debitata = int(input('Ai retras suma de: '))
#         self.sold = self.sold - suma_debitata
#         return print(f'Mai ai in cont: {self.sold} RON.')
#     def creditare_sold(self):
#         suma_creditata = int(input('Ai depus in cont suma de: '))
#         self.sold = self.sold + suma_creditata
#         return print(f'Acum valoare contului este de: {self.sold} RON.')
#
# cont1 = Cont('RO001', 'Popovici Alin', 300)
# cont1.afisare_sold()
# cont1.debitare_cont()
# #Ai retras suma de: 100 => Mai ai in cont: 200 RON.
# cont1.creditare_sold()
# #Ai depus in cont suma de: 50 => Acum valoare contului este de: 250 RON.
#
# cont2 = Cont('RO002', 'Marin Ioan', 1230)
# cont2.afisare_sold()
# cont2.debitare_cont()
# #Ai retras suma de: 75 => Ai retras suma de: 75
# cont2.creditare_sold()
# #Ai depus in cont suma de: 25 => Acum valoare contului este de: 1180 RON.


#        Op.1.

# class Factura:
#     serie = 1234
#     def __init__(self, numar,nume_produs, cantitate, pret_buc):
#
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#     def schimba_cantitatea(self):
#         cantitate = int(input('Scrieti  cantitatea: '))
#         self.cantitate = cantitate
#
#     def schimba_pret(self):
#         pret_buc = int(input('Srieti pretul: '))
#         self.pret_buc = pret_buc
#
#     def schimba_nume_produs(self):
#         nume_produs = str(input('Produsul cumparat este: '))
#         self.nume_produs=nume_produs
#
#     def genereaza_factura(self):
#         print(f'Factura seria {Factura.serie}, numar {self.numar}')
#         from datetime import date
#         today = date.today()
#         print("Data: ", today)
#         print ('Produs | Cantitate | Pret_buc | Total |\n')
#         print (f'{self.nume_produs} |    {self.cantitate}     |     {self.pret_buc}  |  {self.pret_buc * self.cantitate}')
#         print('\n')
#
# factura2 = Factura(1, 'Caiet', 2, 2.5)
# factura2.genereaza_factura()
# print('================================================== =======\n')
# factura2.schimba_cantitatea()
# factura2.schimba_pret()
# factura2.schimba_nume_produs()
# factura2.genereaza_factura()


#       Op.2.
class Masina:
    marca = "Dacia"
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {'alb', 'albastru', 'galben', 'negru', 'verde', 'mov'}
    inmatriculare = False
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print (f'Marca masina : {self.marca}, Model : {self.model}, Viteza actuala: {self.viteza_actuala} km/h, Viteza maxima: {self.viteza_maxima}km/h, Culoare: {self.culoare}, Inmatriculata : {self.inmatriculare}')
    def inmatriculare1(self, inmatriculata):
        self.inmatriculare = inmatriculata
        return print(f'Masina a fost inmatriculata : {self.inmatriculare}')
    def vopseste(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare = culoare_noua
            return print(f'Marina a fost vopsita in culoarea dorita ({self.culoare})')
        else:
            return print(f'Eroare - culoarea dorita nu este disponibila')
    def accelereaza(self, viteza_actuala):
        Masina.viteza_actuala = viteza_actuala
        if viteza_actuala < 0:
            return print('Eroare')
        elif viteza_actuala > self.viteza_maxima:
            return print(f'Masina a accelerat la {self.viteza_maxima}')
        else:
            return print(f'Masina a accelerat la {viteza_actuala} km/h.')
    def franeaza(self):
        Masina.viteza_actuala = 0
        return print(f'Masina s-a oprit.')




masina1 = Masina('Logan', 140)
masina1.descrie()
masina1.inmatriculare1(True)
# masina1.vopseste('visiniu')
# masina1.accelereaza(100)
# masina1.franeaza()
#
# m2 = Masina('Duster', 191)
# m2.descrie()
# m2.inmatriculare(True)
# m2.vopseste('mov')
# m2.accelereaza(200)
# m2.franeaza()

#    op.3
# class ToDoList:
#     todo = {}
#
#     def adauga_task(self, nume, descriere):
#         ToDoList.todo.update({nume : descriere})
#     def finalizeaza_task(self, nume):
#         ToDoList.todo.pop(nume)
#     def afiseaza_todo_list(self):
#         print(ToDoList.todo.keys())
#     def afiseaza_detalii_suplimentare(self, nume):
#         if nume in ToDoList.todo:
#             print(f' {ToDoList.todo[nume]}')
#         else:
#             raspuns = input(f'Taskul nu este in todo list. Vreti sa il adaugam?')
#             if raspuns == 'nu':
#                 print('La revedere!')
#             elif raspuns == 'da':
#                 # detalii_task = input('Spuneti detaliile taskului: ')
#                 ToDoList.todo.update({nume : input('Spuneti detaliile taskului: ')})




# task1 = ToDoList()
# task1.adauga_task('aeriseste camera', 'deschide geamul')
# task1.adauga_task('aranjeaza patul', 'pune patura')
# task1.adauga_task('curata podeaua', 'sterge cu mopul')
# task1.afiseaza_todo_list()
# task1.finalizeaza_task('aeriseste camera')
# task1.afiseaza_todo_list()
# task1.afiseaza_detalii_suplimentare('aranjeaza patul')
# task1.afiseaza_todo_list()
# print(f'\n')
# task2 = ToDoList()
# task2.adauga_task('aeriseste camera', 'deschide geamul')
# task2.adauga_task('aranjeaza patul', 'pune patura')
# task2.adauga_task('curata podeaua', 'sterge cu mopul')
# task2.afiseaza_todo_list()
# task2.finalizeaza_task('aranjeaza patul')
# task2.afiseaza_todo_list()
# task2.afiseaza_detalii_suplimentare('sterge praful')  # Taskul nu este in todo list. Vreti sa il adaugam?da
#                                                       # Spuneti detaliile taskului: cu laveta sterge praful de pe noptiera
# task2.afiseaza_todo_list()
#
