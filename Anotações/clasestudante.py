class Turma:
    def __init__ (self,nome, ):
        self.nome = nome
        self.estudantes = []
    
    def adcionar_estudante(self, estudante):
        self.estudantes.append(estudante)

joao = Estudante("Joao")
maria = Estudante("Turma A")
turmaA.adcionar_estudante(joao)
turmaA.adcionar_estudante(maria)