def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 29.9 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 34.9 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def main():
    peso = input("Digite o seu peso em kg: ")
    altura = input("Digite a sua altura em metros: ")
    
    if peso.replace('.', '', 1).isdigit() and altura.replace('.', '', 1).isdigit():
        peso = float(peso)
        altura = float(altura)
        
        imc = calcular_imc(peso, altura)
        interpretacao = interpretar_imc(imc)
        
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {interpretacao}")
    else:
        print("Entrada inválida. Certifique-se de inserir valores numéricos válidos.")

if __name__ == "__main__":
    main()