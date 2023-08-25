dieimes_matriz = [[3, 4, 1], [3, 2, 1]]

soma_elementos = 0

for linha in dieimes_matriz:
    for elemento in linha:
        soma_elementos += elemento

print("matriz:")
for linha in dieimes_matriz:
    print(linha)
print(f"soma de todos os elementos da matriz: {soma_elementos}")