def show_list(shopping_list):
    print("Lista de Compras:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print()

def main():
    shopping_list = []

    while True:
        print("Escolha uma opção:")
        print("1. Mostrar lista de compras")
        print("2. Adicionar item à lista")
        print("3. Editar item da lista")
        print("4. Remover item da lista")
        print("5. Sair")
        
        num = input("Opção: ")

        if num == "1":
            show_list(shopping_list)
        elif num == "2":
            item = input("Digite o item que deseja adicionar: ")
            shopping_list.append(item)
            print(f"{item} foi adicionado à lista.")
        elif num == "3":
            show_list(shopping_list)
            index = int(input("Digite o número do item que deseja editar: ")) - 1
            if 0 <= index < len(shopping_list):
                new_item = input("Digite o novo valor do item: ")
                shopping_list[index] = new_item
                print("Item editado com sucesso.")
            else:
                print("Índice inválido.")
        elif num == "4":
            show_list(shopping_list)
            index = int(input("Digite o número do item que deseja remover: ")) - 1
            if 0 <= index < len(shopping_list):
                removed_item = shopping_list.pop(index)
                print(f"{removed_item} foi removido da lista.")
            else:
                print("Índice inválido.")
        elif num == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")
if __name__ == "__main__":
    main()