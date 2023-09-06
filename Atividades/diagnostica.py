import tkinter as tk
from tkinter import messagebox

def enviar_mensagem():
    nome = nome_entry.get()
    mensagem = mensagem_entry.get()
    if nome and mensagem:
        janela_mensagem = tk.Toplevel(root)
        janela_mensagem.title("Mensagem Enviada")
        mensagem_label = tk.Label(janela_mensagem, text=f"Seu nome: {nome}\nMensagem: {mensagem}")
        mensagem_label.pack()
    else:
        messagebox.showerror("erro", "por favor, preencha ambos os campos.")

root = tk.Tk()
root.title("Envio de Mensagem")

nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

mensagem_label = tk.Label(root, text="Mensagem:")
mensagem_label.pack()
mensagem_entry = tk.Entry(root)
mensagem_entry.pack()

meu_nome = "Mateus Augusto"  
meu_nome_label = tk.Label(root, text=f"Desenvolvido por: {meu_nome}")
meu_nome_label.pack()

enviar_button = tk.Button(root, text="Enviar", command=enviar_mensagem)
enviar_button.pack()

root.mainloop()

