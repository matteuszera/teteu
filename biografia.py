nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
if idade >= 18:
    maior_idade = True
else:
    maior_idade = False
    print("Informações Pessoais")
print("Nome completo:", nome, sobrenome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Peso:", peso, "kg")
if maior_idade:
    print("Maior de idade: Sim")
else:
    print("Maior de idade: Não")