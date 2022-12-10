# Desafio de Código Atividade do Curso de Python - Orientação a Objetos

## Desafio 2-1
Defina uma classe chamada Pessoa() e que contenha os atributos nome e idade.
Atividade respondida nesse repositorio.

Código que foi disponibilizado:
~~~ python
    if _name__ == "__main__":
        p = Pessoa()
    
        p.nome = input()
        p.idade = input()
    
        print(f"Nome: {p.nome} - Idade: {p.idade}")
~~~


## Desafio 2-2

Defina uma classe chamada PrimeiraClasse(), com um método chamado ola() que exibe no console a mensagem:
"Bem-vindo a orientação à objetos"

Saída esperada: Bem-vindo a orientação à objetos
Código que foi disponibilizado:
~~~ python
    if __name__ == "__main__":
        pc = PrimeiraClasse()
    
        pc.ola();
~~~

## Desafio 3-1

Defina uma classe chamada Curso que receba pelo construtor três atributos: nome, preco e descricao.
Saída esperada: Nome: Python - Preço: 100 - Descrição: Curso de Orientação a Objetos
Código que foi disponibilizado:
~~~ python
    if __name__ == "__main__":
    nome = input()
    preco = input()
    descricao = input()
    c = Curso(nome, preco, descricao)
    
    print(f"Nome: {c.nome} - Preço: {c.preco} - Descrição: {c.descricao}")
~~~

## Desafio 3-2

Complete o código abaixo de forma que seja exibido no console a mensagem "Finalizando execução".
Saída esperada: Finalizando execução
Código que foi disponibilizado:
~~~ python
    if __name__ == "__main__":
    c = MinhaClasse()
    del c)
~~~

## Desafio 4-1

Uma classe chamada Aritmetica, que contenha um método chamado subtracao. Este método deve receber por parâmetro dois valores e retornar a subtração entre eles.
Saída esperada: Minha superclasse é: <class '__main__.Aritmetica'> | Valores de Subtraca
Código que foi disponibilizado:

~~~ python
    if __name__ == "__main__":
    s = Sub()
    
    # Exibe o nome da superclasse
    print("Minha superclasse é: " + str(s.__class__.__bases__[0]))	
    
    t = int(input())
    
    for i in range(0, t):
        var1, var2 = input().split()
        print(s.subtracao(int(var1),int(var2)))
~~~

## Desafio 4-2

* Uma classe chamada Animal, que contém um método chamado andar, que exibe a mensagem: "Estou andando!".
* Uma classe chamada Aquatico, que contém um método chamado nadar, que exibe a mensagem: `"Estou nadando!".
* Uma classe chamada Reptil, que herda as classes Animal e Aquatico.
Saída esperada: Minhas superclasses são: [<class '__main__.Animal'>, <class '__main__.Aquatico'>]
Estou andando!
Estou nadando!
Código que foi disponibilizado:

~~~ python
    if __name__ == "__main__":
    r = Reptil()
    
    # Exibe o nome das superclasses
    print("Minhas superclasses são: " + str(sorted(r.__class__.__bases__, key = lambda x: x.__name__)))	
    
    r.andar()
    r.nadar()
~~~