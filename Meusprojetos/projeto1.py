import tkinter as tk

# Função para realizar o cálculo
def calcular(operador):
    # Obtém os valores digitados nos campos de entrada
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    
    # Realiza o cálculo com base no operador
    if operador == "+":
        resultado = valor1 + valor2
    elif operador == "-":
        resultado = valor1 - valor2
    elif operador == "*":
        resultado = valor1 * valor2
    elif operador == "/":
        if valor2 != 0:  # Verifica se o divisor não é zero
            resultado = valor1 / valor2
        else:
            resultado = "Divisão por zero"
    
    # Atualiza a label com o resultado
    label_resultado.config(text=f"Resultado: {resultado}")

# Cria uma instância da janela principal
janela = tk.Tk()

# Configura o título da janela
janela.title("Calculadora BOLADONA")

# Define o tamanho da janela (largura x altura)
janela.geometry("400x300")

# Cria campos de entrada para os números
entrada1 = tk.Entry(janela)
entrada2 = tk.Entry(janela)

# Cria um frame para conter os botões
frame_botoes = tk.Frame(janela)

# Cria botões para os operadores
botao_soma = tk.Button(frame_botoes, text="+", command=lambda: calcular("+"))
botao_subtracao = tk.Button(frame_botoes, text="-", command=lambda: calcular("-"))
botao_multiplicacao = tk.Button(frame_botoes, text="*", command=lambda: calcular("*"))
botao_divisao = tk.Button(frame_botoes, text="/", command=lambda: calcular("/"))

# Cria uma label para exibir o resultado
label_resultado = tk.Label(janela, text="Resultado: ")

# Exibe os widgets na janela
entrada1.pack()
entrada2.pack()

# Coloca os botões no frame horizontalmente
botao_soma.pack(side="left")
botao_subtracao.pack(side="left")
botao_multiplicacao.pack(side="left")
botao_divisao.pack(side="left")

# Coloca o frame dos botões no centro horizontal da janela
frame_botoes.pack()

label_resultado.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
