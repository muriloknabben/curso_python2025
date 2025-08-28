# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

def multiplica(*arg):
    total = 1
    for num in arg:
        total *= num
    return total

multiplicadores = multiplica(7, 8, 4, 5, 2)
print(multiplicadores)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_impar(num):
    resto2 = num % 2
    if resto2 == 0:
        return 'par'
    return 'ímpar'

resultado = par_impar(9)
print(resultado)