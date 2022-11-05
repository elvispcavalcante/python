from abc import ABC, abstractmethod


class App:
    def __init__(self, nome, consumo_memoria, consumo_bateria):
        self.nome = nome
        self.consumo_memoria = consumo_memoria
        self.consumo_bateria = consumo_bateria


class Smartphone:
    def __init__(self, fabricante, memoria, bateria, consumo_memoria):
        self.fabricante = fabricante
        self.memoria = memoria
        self.bateria = bateria
        self.consumo_memoria = consumo_memoria
        self.ligado = False
        self.apps = []

    def ligar(self):
        if self.ligado:
            print('O smartphone já está ligado')
        else:
            self.ligado = True
            print('O smartphone ligou')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O smartphone desligou')
        else:
            print('O smartphone está desligado')

    @abstractmethod
    def abrirApp(self, nome_aplicativo, consumo_memoria, consumo_bateria):
        pass

    @abstractmethod
    def fecharApp(self, nome_aplicativo):
        pass

    @abstractmethod
    def listarApps(self):
        pass

    def exibirDados(self):
        print('Sobre o Smartphone:')
        print(f'Fabricante: {self.fabricante}')
        print(f'Memória: {self.memoria}')
        print(f'Bateria: {self.bateria}')
        print(f'Consumo da Memória: {self.consumo_memoria}')
        print(f'Ligado: {self.ligado}')
        self.listarApps()


class Xiaomi(Smartphone):
    def __init__(self, fabricante, memoria, bateria, consumo_memoria):
        super().__init__(fabricante, memoria, bateria, consumo_memoria)

    def abrirApp(self, nome_aplicativo, consumo_memoria, consumo_bateria):
        app = App(nome_aplicativo, consumo_memoria, consumo_bateria)
        if self.consumo_memoria + consumo_memoria - consumo_memoria * 0.20 <= self.memoria and self.bateria > 0:
            self.consumo_memoria = self.consumo_memoria + consumo_memoria - consumo_memoria * 0.20
            self.apps.append(app)
        else:
            self.desligar()

    def fecharApp(self, nome_aplicativo):
        for aplicativo in self.apps:
            if aplicativo.nome == nome_aplicativo:
                if self.consumo_memoria - aplicativo.consumo_memoria > 0:
                    self.consumo_memoria = self.consumo_memoria - aplicativo.consumo_memoria
                else:
                    self.consumo_memoria = 0.00
                self.apps.remove(aplicativo)
        self.bateria = self.bateria - (self.bateria * 0.005)

    def listarApps(self):
        if len(self.apps) > 0:
            self.bateria = self.bateria - (self.bateria * 0.005)
            print("Na memória do smartphone tem os seguintes aplicativos: ")
            for app in self.apps:
                print(f"Nome: {app.nome}, Consumo Memória: {app.consumo_memoria}, Consumo Bateria: {app.consumo_bateria}")
        else:
            print('Aplicativos:')
            print('Não há aplicativos na memória no momento!')


class Iphone(Smartphone):
    def __init__(self, fabricante, memoria, bateria, consumo_memoria):
        super().__init__(fabricante, memoria, bateria, consumo_memoria)

    def abrirApp(self, nome_aplicativo, consumo_memoria, consumo_bateria):
        app = App(nome_aplicativo, consumo_memoria, consumo_bateria)
        if self.consumo_memoria + consumo_memoria + consumo_memoria * 0.20 <= self.memoria and self.bateria > 0:
            self.consumo_memoria += consumo_memoria + (consumo_memoria * 0.20)
            self.apps.append(app)
        else:
            self.desligar()

    def fecharApp(self, nome_aplicativo):
        for aplicativo in self.apps:
            if aplicativo.nome == nome_aplicativo:
                aplicacao = aplicativo
                self.consumo_memoria -= aplicativo.consumo_memoria
                self.apps.remove(aplicacao)
        self.bateria -= self.bateria * 0.01

    def listarApps(self):
        self.bateria -= self.bateria * 0.01
        print("Na memória do smartphone tem os seguintes aplicativos: ")
        for app in self.apps:
            print(f"Nome: {app.nome}, Consumo Memória: {app.consumo_memoria}, Consumo Bateria: {app.consumo_bateria}")


xiaomi = Xiaomi('Xiaomi', 100, 100, 0)
iphone = Iphone('Iphone', 200, 100, 0)

xiaomi.ligar()
xiaomi.abrirApp('Camera', 20, 20)
xiaomi.listarApps()
xiaomi.exibirDados()
xiaomi.fecharApp('Camera')
xiaomi.exibirDados()
xiaomi.desligar()

iphone.ligar()
iphone.abrirApp('Camera', 20, 20)
iphone.listarApps()
iphone.exibirDados()
iphone.fecharApp('Camera')
iphone.exibirDados()
iphone.desligar()