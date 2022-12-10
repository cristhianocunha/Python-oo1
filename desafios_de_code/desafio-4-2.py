# Uma classe chamada Animal, que contém um método chamado andar, que exibe a mensagem: "Estou andando!".
# Uma classe chamada Aquatico, que contém um método chamado nadar, que exibe a mensagem: `"Estou nadando!".
# Uma classe chamada Reptil, que herda as classes Animal e Aquatico.
# Saída esperada: Minhas superclasses são: [<class '__main__.Animal'>, <class '__main__.Aquatico'>]
# Estou andando!
# Estou nadando!


class Aquatico():

    def nadar(self):
        print("Estou nadando!")


class Animal():


    def andar(self):
        print("Estou andando!")


class Reptil(Animal, Aquatico):

    def andar(self):
        print("Estou andando!")

# Codigo fornecido

if __name__ == "__main__":
    r = Reptil()

    # Exibe o nome das superclasses
    print("Minhas superclasses são: " + str(sorted(r.__class__.__bases__, key=lambda x: x.__name__)))

    r.andar()
    r.nadar()