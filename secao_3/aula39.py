"""
Iterando strings com while
"""

nome1 = 'Murilo Knabben'  # Iteráveis
tamanho_nome = len(nome1)

nome_res = ''
i = 0
while i < tamanho_nome:
    letra1 = nome1[i]
    nome_res += f'*{letra1}'
    i += 1

print(nome_res)


#resolução do professor:


nome2 = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome2):
    letra2 = nome2[indice]
    novo_nome += f'*{letra2}'
    indice += 1

novo_nome += '*'
print(novo_nome)