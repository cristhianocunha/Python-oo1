import abc


class InterfaceVeiculo(abc.ABC):

    @abc.abstractmethod
    def show_tipo(self):
        pass


# Coloque seu código aqui
class Carro(InterfaceVeiculo):

    def show_tipo(self):
        print("Carro")


class Moto(InterfaceVeiculo):
    def show_tipo(self):
        print("Moto")


if __name__ == "__main__":
    c = Carro()

    c.show_tipo()

    c = Moto()

    c.show_tipo()