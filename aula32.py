"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

valor = input('Digite um número inteiro: ')

try:
    num_int = int(valor)
    if num_int % 2 == 0:
        print('Seu número é par.')

    else:
        print('Seu número é ímpar.')

except:
    print('Digite um número inteiro por favor.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite que horas são: ')

try:
    hora_int = int(hora)

    if 0 <= hora_int < 12:
        print('Bom dia!')

    elif 12 <= hora_int < 18:
        print('Boa tarde!')

    elif 18 <= hora_int < 24:
        print('Boa noite!')

    else:
        print('Por favor digite uma hora valida.')

except:
    print('Por favor digite apenas a hora')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

p_nome = input('Digite seu primeiro nome: ')

if p_nome:

    tamanho = len(p_nome)

    if tamanho <= 4:
        print('Seu nome é curto!')

    elif tamanho <=6:
        print('Seu nome é normal.')

    else:
        print('Seu nome é muito grande!')

else:
    print('Por favor digite seu primeiro nome')