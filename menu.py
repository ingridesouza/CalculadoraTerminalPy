from funcoes import somar,subtrair,multiplicar,dividir

while True:
    
    opcoes = input(
        '''
        Selecione a Operação:
        ---------------------
        + Somar
        - Subtrair
        * Multiplicar
        / Dividir
        S Sair
        ---------------------
        '''
    ).upper()
    
    # x = int(input('Digite o primeiro número: '))
    # y = int(input('Digite o segundo número: '))
    
    match opcoes:
        case '+':
            numero1 = int(input('Digite o primeiro número: '))
            numero2 = int(input('Digite o segundo número: '))
            print(f'O resultado é: {somar(numero1,numero2)}')
            
            
        case '-':
            numero1 = int(input('Digite o primeiro número: '))
            numero2 = int(input('Digite o segundo número: '))
            print(f'O resultado é: {subtrair(numero1,numero2)}')
            
        case '*':
            numero1 = int(input('Digite o primeiro número: '))
            numero2 = int(input('Digite o segundo número: '))
            print(f'O resultado é: {multiplicar(numero1,numero2)}')
            
        case '/':
            numero1 = int(input('Digite o primeiro número: '))
            numero2 = int(input('Digite o segundo número: '))
            print(f'O resultado é: {dividir(numero1,numero2)}')
            
        case 'S':
            print('Saindo....')
            break
        
        case _:
            print('Operação Inválida!')