while True:
    operacao = input('Digite "a" para contas de adição\nDigite "m" para contas de menos\nDigite "v" para contas de vezes\nDigite "d" para contas de divisão\nDigite "s" para sair\nO que deseja: ')
    operacao = operacao.lower()
    if operacao in ('a', 'm', 'v', 'd'):
        try:
            a = input('Digite o primeiro numero: ')
            b = input('Digite o segundo número: ')
            a = float(a)
            b = float(b)
        except ValueError:
            print('Por favor digite um número')

    elif operacao == 'a':
        c = a + b
        print(f'{a} + {b} = {c}')
    
    elif operacao == 'm':
            c = a - b
            print(f'{a} - {b} = {c}')

    elif operacao == 'v':
            c = a * b
            print(f'{a} x {b} = {c}')

    elif operacao == 'd':
        if b == 0:
            print('Divisão por 0 não é possivel, por favor digite uma operção válida')
            
        else:
            c = a / b
            print(f'{a} / {b} = {c}')

    elif operacao == 's':
        break

    else:
        print('Por favor digite uma opção válida')