nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if idade != '' and nome != '':
    nome_invertido = nome[::-1]
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome_invertido}')
    if ' ' in nome:
        print('Seu nome tem espaços')

    else:
        print('Seu nome não tem espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {primeira_letra}')
    print(f'A última letra do seu nome é: {ultima_letra}')

else:
    print('Desculpe, você deixou espaços vazios')