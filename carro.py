import automovel


class Carro(automovel.veiculo):


    def __init__(self, nome, cor, combustivel, potencia, qtd_tanque, portas ):
        super().__init__(nome, cor, combustivel, potencia, qtd_tanque)
        self.portas = portas
        self._libra = 30

    def verificar_libra(self):
        print(f"libra do pneus da Carro é {self._libra}")

    def pintar(self, cor):
        if cor == "preto":
            print('não pode pintar carro de preto')
        else:
            self._cor = cor