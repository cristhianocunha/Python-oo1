# Complete o código abaixo de forma que seja exibido no console a mensagem "Finalizando execução".
# Saída esperada: Finalizando execução

class MinhaClasse:

    def __del__(self):
        print("Finalizando execução")


if __name__ == "__main__":
    c = MinhaClasse()
    del c