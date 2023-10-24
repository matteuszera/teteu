import tkinter as tk

# Função a ser executada quando o botão for clicado
def botao_clicado():
    botao.config(text="Botão Clicado")

# Cria uma instância da janela principal
janela = tk.Tk()

# Configura o título da janela
janela.title("Meu Primeiro projeto")

# Define o tamanho da janela (largura x altura)
janela.geometry("400x300")

# Cria um botão
botao = tk.Button(janela, text="Clique em Mim", command=botao_clicado)

# Exibe o botão na janela
botao.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
