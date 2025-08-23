while True:
    operacao = input('Digite "a" para contas de adição\nDigite "m" para contas de menos\nDigite "v" para contas de vezes\nDigite "d" para contas de divisão\nDigite "s" para sair\nO que deseja: ')
    operacao = operacao.lower()

    if operacao == 'a':
        try:
            a = input('Digite o primeiro numero: ')
            b = input('Digite o segundo número: ')
            a = float(a)
            b = float(b)
            c = a + b
            print(f'{a} + {b} = {c}')
        except ValueError:
            print('Por favor digite um número')
    
    elif operacao == 'm':
        try:
            a = input('Digite o primeiro numero: ')
            b = input('Digite o segundo número: ')
            a = float(a)
            b = float(b)
            c = a - b
            print(f'{a} - {b} = {c}')
        except ValueError:
            print('Por favor digite um número')

    elif operacao == 'v':
        try:
            a = input('Digite o primeiro numero: ')
            b = input('Digite o segundo número: ')
            a = float(a)
            b = float(b)
            c = a * b
            print(f'{a} x {b} = {c}')
        except ValueError:
            print('Por favor digite um número')

    elif operacao == 'd':
        try:
            a = input('Digite o primeiro numero: ')
            b = input('Digite o segundo número: ')
            a = float(a)
            b = float(b)
            if b == 0:
                print('Divisão por 0 não é possivel, por favor digite uma operção válida')
            
            else:
                c = a / b
                print(f'{a} / {b} = {c}')
        except ValueError:
            print('Por favor digite um número')

    elif operacao == 's':
        break

    else:
        print('Por favor digite uma opção válida')