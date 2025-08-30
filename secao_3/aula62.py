"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

while True:
    cpf = input('Digite o CPF a ser validado: ')
    cpf_limpo = cpf.replace(".", "").replace("-", "")

    if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
        print('CPF inválido, por favor digite 11 números.')
        continue

    numeros = []
    for d in cpf_limpo:
        numeros.append(int(d))

    soma1 = 0
    contador = 10
    for i in range(9):
        soma1 += numeros[i] * contador
        contador -= 1

    resto1 = (soma1 * 10) % 11
    if resto1 == 10:
        resto1 = 0

    if numeros[9] != resto1:
        print('CPF inválido.')
        continue

    soma2 = 0
    contador = 11
    for i in range(10):
        soma2 += numeros[i] * contador
        contador -= 1

    resto2 = (soma2 * 10) % 11
    if resto2 == 10:
        resto2 = 0

    if numeros[10] != resto2:
        print('CPF inválido.')
    else:
        print('CPF válido.')