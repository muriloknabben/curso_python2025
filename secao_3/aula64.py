import random
import os

while True:
    resposta = input('Quer gerar um CPF?\n[s]im ou [n]ão\n')
    if resposta == 's':
        os.system('cls')
        nove_digitos = ''

        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        numeros = []
        for d in nove_digitos:
            numeros.append(int(d))

        soma1 = 0
        contador = 10
        for i in range(9):
            soma1 += numeros[i] * contador
            contador -= 1

        resto1 = (soma1 * 10) % 11

        if resto1 == 10:
            numeros.append(0)

        else:
            numeros.append(resto1)

        soma2 = 0
        contador = 11
        for i in range(10):
            soma2 += numeros[i] * contador
            contador -= 1

        resto2 = (soma2 * 10) % 11

        if resto2 == 10:
            numeros.append(0)

        else:
            numeros.append(resto2)

        cpf = ''.join([str(n) for n in numeros])
        print(f'CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:12]}')

    
    elif resposta == 'n':
        os.system('cls')
        break

    else:
        os.system('cls')
        print('Por favor digite "s" ou "n"')