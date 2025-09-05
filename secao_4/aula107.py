# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from dados_secao4 import cidades, estados


# def zipper(cidades, estados):
#     intervalo = min(len(cidades), len(estados))
#     return [(cidades[i], estados[i]) for i in range(intervalo)]
from itertools import zip_longest
print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE')))

# unir duas listas:

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)