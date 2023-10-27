class Cabeça:
    def __init__(self, tipo_cabelo, cor_olhos):
        self.tipo_cabelo = tipo_cabelo
        self.cor_olhos = cor_olhos

    def descrever(self):
        print(f"Cabeça com cabelos {self.tipo_cabelo} e olhos de cor {self.cor_olhos}.")

class Boneco:
    def __init__(self, nome, idade, tipo_cabelo, cor_olhos):
        self.nome = nome
        self.idade = idade
        self.cabeça = Cabeça(tipo_cabelo, cor_olhos)

    def destruir(self):
        print(f"O boneco {self.nome} foi destruído e sua cabeça também.")
        del self

    def descrever(self):
        print(f"Boneco {self.nome}, {self.idade} anos de idade:")
        self.cabeça.descrever()


boneco1 = Boneco("João", 5, "castanho", "azul")
boneco2 = Boneco("Maria", 8, "loiro", "verde")

boneco1.descrever()
boneco2.descrever()

boneco1.destruir()

