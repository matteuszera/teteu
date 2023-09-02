alunos = {}


for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    alunos[nome] = nota

soma_notas = sum(alunos.values())

media = soma_notas / len(alunos)

print(f"A média das notas dos alunos é: {media:.2f}")
