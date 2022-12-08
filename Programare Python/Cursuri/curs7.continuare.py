class Masina:
    # definire atribute
    model = None
    culoare = 'Orange'
    marca = None
    viteza_maxima = 0
    an_fabricatie = 0
    capacitate_motor = 0
    serie_sasiu = None
    tip_combustibil = 'motorina'
    cutie_viteza = 'automat'
    viteza_curenta = 0

    # metode
    # 1. constructor
    # def __init__(self, marca1, model1, culoare1):
    #     self.marca = marca1
    #     self.model = model1
    #     if culoare1 == 'orange':
    #         self.culoare = 'portocaliu'
        # self.culoare = culoare1

    # metode
    def paint(self,colour):
        self.colour = colour

    def start_masina(self):
        self.viteza_curenta = self.viteza_curenta + 5
        print('Masina s-a pus in miscare.')
        return self.viteza_curenta

bmw = Masina()
bmw.culoare = 'galben'
print(bmw.culoare)
print(bmw.marca)
bmw.paint('Verde')
print(bmw.culoare)
print(bmw.start_masina())





