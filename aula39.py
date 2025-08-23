"""
Iterando strings com while
"""

nome = 'Murilo Knabben'  # Iteráveis
tamanho_nome = len(nome)

i = 0
while i < tamanho_nome:
    letra = nome[i]
    print(f"Caractere {i}: {letra}")
    i += 1