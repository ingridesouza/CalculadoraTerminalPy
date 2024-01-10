# Crie um programa que será uma calculadora.

# Nesta calculadora você deverá ter um módulo para as
# operações matemáticas, o arquivo principal deverá
# conter apenas um menu de escolha para o usuário

# (soma, subtração, multiplicação e divisão).
#funcoes verbos no infinitivo

def somar(x:float,y:float)-> float:
    return x + y

def subtrair(x:float,y:float)-> float:
    return x - y

def multiplicar(x:float,y:float)-> float:
    return x * y

def dividir(x:float,y:float)-> str:
    if y==0:
        return 'Erro, divisão por zero!'
    else:
        result = x/y
        return f'{result:.2f}'









# :.2f = formatação no número, para não aparecer uma dizima, aparece apenas 3 números

# uma função é um bloco de código que realiza uma tarefa específica. Ela é definida usando a palavra-chave def , seguida pelo nome da função e parênteses. As funções oferecem uma maneira de organizar e reutilizar código, promovendo a legibilidade e a eficiência.

# match case = podemos construir um bloco de comandos com múltiplas possibilidades de decisão, que compara uma expressão com uma série de valores e retorna uma instrução.