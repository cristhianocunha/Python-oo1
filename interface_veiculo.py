import abc

class InterfaceVeiculo(abc.ABC):


    @abc.abstractmethod
    def pintar(self, cor):
        pass

    @abc.abstractmethod
    def abastecer(self, litros):
        pass

    @abc.abstractmethod
    def ligar(self):
        pass

    @abc.abstractmethod
    def deligar(self):
        pass

    @abc.abstractmethod
    def acelerar(self, velocidade=10):
        pass

    @abc.abstractmethod
    def verificar_libra(self):
        pass