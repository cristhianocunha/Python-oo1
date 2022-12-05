import automovel
import carro, moto

#(self, cor, portas, combustivel, potencia, qtd_tanque, qt_combustivel, is_ligado, velocidade):

Peugeot = carro.Carro("206", "Cinza", "Flex", 1.6, 50, 2)
mto_azul = moto.Moto("honda", "azul", "Gasolina", 1.0, 15, 2)

mto_azul.ligar()


Peugeot.ligar()
mto_azul.verificar_libra()

mto_azul.pintar("preto")

print (mto_azul.cor)
if isinstance(mto_azul, automovel.veiculo):
    print("a classe é um veiculo")
else:
    print("a classe não é um veiculo")


