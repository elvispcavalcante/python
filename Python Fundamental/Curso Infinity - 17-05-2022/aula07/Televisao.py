class Televisao:
    def __init__(self, qtde_canais:int, canal_atual:int, volume_max:int, volume_atual:int, ligado=False):
        self.qtde_canais = qtde_canais
        self.canal_atual = canal_atual
        self.volume_max = volume_max
        self.volume_atual = volume_atual
        self.ligado = ligado

    def ligarTV(self):
        self.ligado = True
        print("A TV está ligada!")

    def desligarTV(self):
        self.ligado = False
        print("A TV está desligada!")

    def mudar_canal_mais(self):
        if self.ligado == True:
            if self.canal_atual < self.qtde_canais:
                self.canal_atual += 1
                print(f"O canal atual é o {self.canal_atual}")
            else:
                self.canal_atual = 1
                print(f"O canal atual é o {self.canal_atual}")
        else:
            print("A Tv está desligada")

    def mudar_canal_menos(self):
        if self.ligado == True:
            if self.canal_atual <= 1:
                self.canal_atual = self.qtde_canais
                print(f"O canal atual é o {self.canal_atual}")
            else:
                self.canal_atual -= 1
                print(f"O canal atual é o {self.canal_atual}")
        else:
            print("A Tv está desligada")

    def aumentar_volume(self):
        if self.ligado == True:
            if self.volume_atual < self.volume_max:
                self.volume_atual += 1
                print(f"Você está no volume {self.volume_atual}")
            else:
                self.volume_atual = self.volume_max
                print("Você chegou no volume máximo")
        else:
            print("A Tv está desligada")

    def diminuir_volume(self):
        if self.ligado == True:
            if self.volume_atual >= 0 and self.volume_atual <= self.volume_max:
                self.volume_atual -= 1
                print(f"Você está no volume {self.volume_atual}")
            else:
                self.volume_atual = 0
                print("Você chegou no volume máximo")
                print(f"Você está no volume {self.volume_atual}")
        else:
            print("A Tv está desligada")


criartv = Televisao(10, 2, 10, 5)

criartv.ligarTV()

criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()
criartv.mudar_canal_mais()

criartv.mudar_canal_menos()
criartv.mudar_canal_menos()
criartv.mudar_canal_menos()
criartv.mudar_canal_menos()
criartv.mudar_canal_menos()
criartv.mudar_canal_menos()


criartv.aumentar_volume()
criartv.aumentar_volume()
criartv.aumentar_volume()
criartv.aumentar_volume()
criartv.aumentar_volume()
criartv.aumentar_volume()

criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()
criartv.diminuir_volume()


criartv.desligarTV()


