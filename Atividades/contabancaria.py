class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def ver_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")


conta_exemplo = ContaBancaria("João")

conta_exemplo.depositar(1000)
conta_exemplo.sacar(300)
conta_exemplo.depositar(500)
conta_exemplo.sacar(800)


conta_exemplo.ver_saldo()
