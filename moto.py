import automovel
class Moto(automovel.veiculo):

    def __init__(self, nome, cor, combustivel, potencia, qtd_tanque, qt_passageiro):
        super().__init__(nome, cor, combustivel, potencia, qtd_tanque)
        self.qt_passageiro = qt_passageiro
        self._libra = 25

    def verificar_libra(self):
        print(f"libra do pneus da moto é {self._libra}")

    def pintar(self, cor):
        if cor == "preto":
            print('não pode pintar moto de preto')
        else:
            self._cor = cor
