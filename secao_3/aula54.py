"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('[i]nserir [a]pagar [l]ista [s]air')
    acao = input('O que deseja: ')
    acao = acao.lower()

    if acao in ('i', 'a', 'l', 's'):
        os.system('cls')
    
    if acao == 'i':
        item = input('O que deseja inserir? ')
        lista.append(item)

    elif acao == 'a':
        item_del = input('Que item deseja deletar: ')
        try:
            item_del = int(item_del)
            del lista[item_del]

        except ValueError:
            print('Digite o número do item, por favor')

        except IndexError:
            print('Por favor digite um número válido')

        except Exception:
            print('Erro desconhecido')

    elif acao == 'l':
        if not lista:
            print("A lista está vazia")
        else:
            for indice, produto in enumerate(lista):
                print(indice, produto)

    elif acao == 's':
        print('Tchau!')
        break

    else:
        print('Por favor digite uma das três opções')