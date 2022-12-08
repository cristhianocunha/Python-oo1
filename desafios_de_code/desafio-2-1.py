# Defina uma classe chamada Pessoa() e que contenha os atributos nome e idade.
# Entrada de dados
# Você não será responsável pela entrada.
# Saída esperada
# Você não será responsável pela saída.


# Informe sua classe aqui
class Pessoa():
    def __init__(self):
        self.nome = ""
        self.idade = ""


if __name__ == "__main__":
    p = Pessoa()

    p.nome = input()
    p.idade = input()

    print(f"Nome: {p.nome} - Idade: {p.idade}")