from biblioteca import Pessoa, Cachorro, Gato, Coelho, Vaca, Animal, Ingresso

aluno01=Pessoa("Diego",29, 84)
aluno02=Pessoa("caleb",25, 75)
aluno03=Pessoa("Ruy",24, 78)
'''print(aluno01.nome)
print(aluno01.idade)
print(aluno01.peso)'''

Mascote=Animal("Milo","branca")
Mascote.comer()

bixo=Gato("Milo","branca")
bixo.miar()

cinema=Ingresso(20)
cinema.imprimeValor()
cineVip=Vip(20)
cineVip.imprimeValor()