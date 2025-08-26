"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    acao = input('O que deseja:\n[i]nserir [a]pagar [l]ista [s]air\n')
    acao = acao.lower()
    
    if acao == 'i':
        item = input('O que deseja inserir? ')
        lista.append(item)

    elif acao == 'a':
        item_del = input('Que item deseja deletar: ')
        try:
            item_del = int(item_del)
            del lista[item_del]

        except:
            print('Digite o número do item, por favor')

    elif acao == 'l':
        for indice, produto in enumerate(lista):
            print(indice, produto)

    elif acao == 's':
        break

    else:
        print('Por favor digite uma das três opções')