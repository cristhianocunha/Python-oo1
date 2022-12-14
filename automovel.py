import abc, interface_veiculo


class veiculo(interface_veiculo.InterfaceVeiculo, abc.ABC):

    """"Essa é a classe veiculo, Esta classe é ultilizada para instanciar novos veiculos em nosso programa"""
    def __init__(self, nome, cor, combustivel, potencia, qtd_tanque):
        self.__nome = nome
        self._cor = cor
        self.__combustivel = combustivel
        self.__potencia = potencia
        self.__qtd_tanque = qtd_tanque
        self.__is_ligado = False
        self.__velociade = 0
        self.__qt_combustivel = 1
        self._libra = 0

    @property
    def cor(self):
        return self._cor
    def pintar(self, cor):
        self._cor = cor
        print(f"o {self.__nome} esta pintado na cor {self._cor}")

    def __del__(self):
        print("objeto foi removido da memoria")

    def abastecer(self, litros):
        """"O método abastecer """
        diferan = self.__qtd_tanque - self.__qt_combustivel
        if litros <= diferan:
            self.__qt_combustivel += litros
        else:
            print("Quantidade de litro é maior do que taque.")

    def ligar(self):
        if self.ligar:
            print("Veiculo  esta ligado")
            self.__is_ligado = True
        else:
            self.__is_ligado = True
            print("Veiculo foi ligado")

    def deligar(self):
        if self.__is_ligado == False:
            print("O Veiculo estra desligado")
        else:
            self.__is_ligado = False
    def acelerar(self, velocidade=10):
        if self.__is_ligado:
            self.__velociade += velocidade

        else:
            print("carro esta deligado")
    def verificar_libra(self):
        print(f"quantida de libra no pneus é {self._libra}")