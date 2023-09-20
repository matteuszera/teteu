lista_de_compras = []

def adicionar_item(item):
    lista_de_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")


def apagar_item(item):
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f"{item} foi removido da lista de compras.")
    else:
        print(f"{item} não está na lista de compras.")


def editar_item(item_antigo, item_novo):
    if item_antigo in lista_de_compras:
        indice = lista_de_compras.index(item_antigo)
        lista_de_compras[indice] = item_novo
        print(f"{item_antigo} foi editado para {item_novo} na lista de compras.")
    else:
        print(f"{item_antigo} não está na lista de compras.")

def listar_itens():
    if lista_de_compras:
        print("Lista de Compras:")
        for item in lista_de_compras:
            print(item)
    else:
        print("A lista de compras está vazia.")

while True:
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Apagar item")
    print("3. Editar item")
    print("4. Listar itens")
    print("5. Sair")
    
    escolha = input("Escolha uma opção (1/2/3/4/5): ")
    
    if escolha == "1":
        item = input("Digite o item que deseja adicionar: ")
        adicionar_item(item)
    elif escolha == "2":
        item = input("Digite o item que deseja apagar: ")
        apagar_item(item)
    elif escolha == "3":
        item_antigo = input("Digite o item que deseja editar: ")
        item_novo = input("Digite o novo valor: ")
        editar_item(item_antigo, item_novo)
    elif escolha == "4":
        listar_itens()
    elif escolha == "5":
        print("Saindo do programa.")
        break
    else:
        print("opção invalida. Por favor, escolha uma opção válida (1/2/3/4/5).")
