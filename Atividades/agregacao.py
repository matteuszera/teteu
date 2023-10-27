class Monitor:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def exibir_informacoes(self):
        print(f"Monitor {self.marca}, Tamanho: {self.tamanho} polegadas")

class Computador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.monitor = None  

    def conectar_monitor(self, monitor):
        if isinstance(monitor, Monitor):
            self.monitor = monitor
            print(f"Monitor {monitor.marca} conectado ao computador {self.marca} {self.modelo}.")
        else:
            print("O objeto passado não é um monitor válido.")

    def exibir_informacoes(self):
        print(f"Computador {self.marca} {self.modelo}")
        if self.monitor:
            self.monitor.exibir_informacoes()
        else:
            print("Nenhum monitor conectado a este computador.")


monitor1 = Monitor("Dell", 27)
monitor2 = Monitor("HP", 24)

computador1 = Computador("Lenovo", "ThinkPad")
computador2 = Computador("HP", "Pavilion")

computador1.conectar_monitor(monitor1)

computador1.exibir_informacoes()
computador2.exibir_informacoes()
