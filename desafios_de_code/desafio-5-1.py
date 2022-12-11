# Defina uma classe chamada Pessoa() e que contenha os atributos nome e idade.

# Informe sua classe aqui
class Pessoa():
    def __init__(self):
        self.nome = ""
        self.idade = ""


# FIM Informe sua classe aqui
if __name__ == "__main__":
    p = Pessoa()

    p.nome = input()
    p.idade = input()

    print(f"Nome: {p.nome} - Idade: {p.idade}")