from abc import ABC
class FormaGeometrica(ABC):
    pi = 3.14

    def aria(self):
        pass
    def descrie(self):
        print('Cel mai probabil am colturi.')

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura
    def get_latura(self):
        return print(self.__latura)
    def set_latura(self,latura_noua):
        self.__latura = latura_noua
        return print(latura_noua)
    def del_latura(self):
        self.__latura = None
        return print(self.__latura)
    def aria(self):
      pass

class Cerc(FormaGeometrica):
    _raza = 0
    def __init__(self, _raza):
        self._raza = _raza
    def get_raza(self):
        return self._raza
    def set_raza(self, noua_raza):
        self._raza = noua_raza
        return self._raza
    def delete_raza(self):
        self._raza = None
        return self._raza
    def aria(self):
        aria = self.pi * self._raza ** 2
        return aria
    def descrie(self):
        print('Eu nu am colturi!')




f1 = FormaGeometrica()
f1.aria()
f1.descrie()
print('____________________________________')
p1 = Patrat(3)
p1.get_latura()
p1.set_latura(5)
p1.del_latura()
print('_________________________________')
c1 = Cerc(2)
c1.get_raza()
print(c1.aria())
c1.set_raza(4)
print(c1.aria())
print(c1.delete_raza())
c1.descrie()









