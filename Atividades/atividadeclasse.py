class Estudante:
    def __init__ (self, nome, idade):
          self. nome = nome
          self. idade = idade 
    def texto(self):
        print(f"O meu nome é {self.nome} e minha idade é {self.idade}")   

Aluno = Estudante("Mateus", "19 anos")

print(Aluno.nome)
print(Aluno.idade)

Aluno.texto() 