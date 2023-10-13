class Carro:
    pneus = 4 #atributo da classe
    
    def __init__ (self, marca, modelo):
        self. marca = marca
        self. modelo = modelo 
carro1 = Carro("Ford", "fiesta")
carro2 = Carro("Honda", "Civic")

print(carro1.pneus)
print(carro2.pneus)

print(Carro.pneus)

class turma:
    def __init__ (self, nome, sobrenome):
       self. nome = nome
       self. sobrenome = sobrenome 

    def texto(self):
        print(f"O meu nome é {self.nome} e meu sobrenome é {self.sobrenome}") 

aluno1 = turma("Mateus", "Augusto")

print(aluno1.nome)
print(aluno1.sobrenome)

aluno1.texto()
    