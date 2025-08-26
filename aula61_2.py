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
    cpf = input('Dgite o CPF a ser validado: ')
    cpf_limpo = cpf.replace(".", "").replace("-", "")

    if len(cpf_limpo) != 11:
        print('Você colocou digitos a mais ou a menos no seu CPF, por favor digite novamente.')
        continue

    if not cpf_limpo.isdigit():
        print('Digite apenas números.')
        continue

    ultimos = cpf_limpo[9:]
    nove_digito = cpf_limpo[:9]
    lista_ult = [int(d) for d in ultimos]

    resultado = 0
    contador = 10
    for digito in nove_digito:
        resultado += int(digito) * contador
        contador -= 1
    
    resto = (resultado * 10) % 11

    valido = False
    if resto > 9:
        if lista_ult[0] == 0:
            valido = True

        else:
            print('CPF inválido.')
            continue

    else:
        if lista_ult[0] == resto:
            valido = True

        else:
            print('CPF inválido.')
            continue

    if valido == True:
        dez_digito = cpf_limpo[:10]

        novo_resultado = 0
        contador11 = 11
        for di in dez_digito:
            novo_resultado += int(di) * contador11
            contador11 -= 1

        novo_resto = (novo_resultado * 10) % 11

        if resto > 9:
            if lista_ult[1] == 0:
                print('CPF válido')

            else:
                print('CPF inválido.')

        else:
            if lista_ult[1] == novo_resto:
                print('CPF válido')

            else:
                print('CPF inválido.')