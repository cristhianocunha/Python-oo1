import re
import inspect


class Carro():

    def __init__(self, tipo):
        self.__nome = nome
        self.__tipo = "Sedan"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def tipo(self):
        return self.__tipo


if __name__ == "__main__":
    nome = input()
    tipo = input()

    c = Carro(tipo)
    c.nome = nome

    elementos = dict(vars(Carro))

    ## Membros da classe
    filtro = filter(lambda e: False if re.search(r'\b__\w+__\b', e) else True, dir(c))
    for membro in filtro:
        print(membro)
        if (membro in elementos):
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fget']))
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fset']))

    print(c.nome)
    print(c.tipo)