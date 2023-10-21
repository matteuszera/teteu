class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

    def mostrar_endereco(self):
        return f"{self.rua}, {self.cidade}"

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mostrar_informacoes(self):
        return f"{self.nome} mora em {self.endereco.mostrar_endereco()}"

endereco_maria = Endereco("Av. Principal", "São Paulo")
maria = Pessoa("Maria", endereco_maria)

print(maria.mostrar_informacoes())
