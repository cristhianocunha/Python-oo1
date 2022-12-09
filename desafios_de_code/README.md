# Desafio de Código Atividade do Curso de Python - Orientação a Objetos

## Desafio 2-1
Defina uma classe chamada Pessoa() e que contenha os atributos nome e idade.
Atividade respondida nesse repositorio.

Código que foi disponibilizado:

    if _name__ == "__main__":
        p = Pessoa()
    
        p.nome = input()
        p.idade = input()
    
        print(f"Nome: {p.nome} - Idade: {p.idade}")


## Desafio 2-2

Defina uma classe chamada PrimeiraClasse(), com um método chamado ola() que exibe no console a mensagem:
"Bem-vindo a orientação à objetos"

Saída esperada: Bem-vindo a orientação à objetos
Código que foi disponibilizado:

    if __name__ == "__main__":
        pc = PrimeiraClasse()
    
        pc.ola();

## Desafio 3-1

Defina uma classe chamada Curso que receba pelo construtor três atributos: nome, preco e descricao.
Saída esperada: Nome: Python - Preço: 100 - Descrição: Curso de Orientação a Objetos
Código que foi disponibilizado:

    if __name__ == "__main__":
    nome = input()
    preco = input()
    descricao = input()
    c = Curso(nome, preco, descricao)
    
    print(f"Nome: {c.nome} - Preço: {c.preco} - Descrição: {c.descricao}")


## Desafio 3-2

Complete o código abaixo de forma que seja exibido no console a mensagem "Finalizando execução".
Saída esperada: Finalizando execução
Código que foi disponibilizado:

    if __name__ == "__main__":
    c = MinhaClasse()
    del c)