# Uma classe chamada Aritmetica, que contenha um método chamado subtracao. Este método deve receber por parâmetro dois valores e retornar a subtração entre eles.
# Uma classe chamada Sub, que herde a classe Aritmetica.
# Saída esperada:  Minha superclasse é: <class '__main__.Aritmetica'> | Valores de Subtração


class Aritmetica():
     def subtracao(self, var1, var2):
         return var1 - var2

class Sub(Aritmetica):

   pass

if __name__ == "__main__":
    s = Sub()

    # Exibe o nome da superclasse
    print("Minha superclasse é: " + str(s.__class__.__bases__[0]))

    t = int(input())

    for i in range(0, t):
        var1, var2 = input().split()
        print(s.subtracao(int(var1) ,int(var2)))