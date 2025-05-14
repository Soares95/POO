from symtable import Class


class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comer=False
        self.falar=False
        self.durmir=False

    def comer(self, comida):
        print(f"comer {comida}")
    def durmir(self, tarde):
        print(f"durmir {tarde}")
    def falar(self, poesia):
        print(f"falar {poesia}")

    def comer(self):
        if not self.durmindo and not self.falando:
            self.comendo=True
            print(f"ele esta ")
        elif self.durmindo:
            print

class Animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f" o {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f" o {self.nome} corre atrás de mosca e late...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def cararejar(self):
        print(f" o {self.nome} foi cacarejou...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def mugir(self):
        print(f" o {self.nome} mugiu...")

    def comer(self):
        print(f"O {self.nome} foi comer capim...")

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
        super().__init__(valor)
    def imprimeValor(self):
        print(f" o ingresso custou {self.valor:.2f} ")
class Vip():
    def __init__(self, valor):
        super().__init__(valor*1.5)
    def imprimeValor(self):
        print(f" o ingresso VIP custou {self.valor:.2f} ")

class Forma:
    def __init__(self):
        self.area=0
        self.perimetro=0

class Triangulo:
    def __init__(self, altura):
        super().__init__(altura)
    def calcularArea(self):
    def calcularPerimetro(self):

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calcularArea(selfself,base,altura):
        self.area=base*altura
        print(f"A Area do retangulo é {self.area}")
    def calcularPerimetro(self, base, altura):
        self.perimetro=(base+altura)*2
        print(f"O perimetro do retangulo é {self.perimetro} ")
        
