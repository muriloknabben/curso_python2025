# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

#versão sem json:

# import os

#def listar(lista):
#    if lista:
#        return '\n'.join(f'{i}. {tarefa}' for i, tarefa in enumerate(lista, start=1))
#    return 'Sua lista está vazia.'

#def desfazer(lista, refazer):
#    if lista:
#        refazer.append(lista.pop())
#        return 'Última tarefa desfeita.'
#    return 'Não há o que desfazer.'

#def refazer(lista, refazer):
#    if refazer:
#        lista.append(refazer.pop())
#        return 'Última tarefa refeita.'
#    return 'Não há o que refazer.'

#def adicionar(lista, tarefa):
#    lista.append(tarefa)
#    return f'Tarefa "{tarefa}" adicionada.'

#tarefa = []
#tarefa_refazer = []
    
#while True:
#    print('Comandos: listar, desfazer e refazer')
#    desejo = input('Digite uma tarefa ou comando: ')
#    match(desejo):
#        case 'listar':
#            os.system('cls')
#            print(listar(tarefa))
#        case 'desfazer':
#            os.system('cls')
#            print(desfazer(tarefa, tarefa_refazer))
#        case 'refazer':
#            os.system('cls')
#            print(refazer(tarefa, tarefa_refazer))
#        case _:
#            os.system('cls')
#            print(adicionar(tarefa, desejo))

#versão com json

import os
import json

def listar(lista):
    if lista:
        return '\n'.join(f'{i}. {tarefa}' for i, tarefa in enumerate(lista, start=1))
    return 'Sua lista está vazia.'

def desfazer(lista, refazer):
    if lista:
        refazer.append(lista.pop())
        return 'Última tarefa desfeita.'
    return 'Não há o que desfazer.'

def refazer(lista, refazer):
    if refazer:
        lista.append(refazer.pop())
        return 'Última tarefa refeita.'
    return 'Não há o que refazer.'

def adicionar(lista, tarefa):
    lista.append(tarefa)
    return f'Tarefa "{tarefa}" adicionada.'

def ler(tarefas, caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho)
    return dados

def salvar(tarefas, caminho):
    dados = tarefas
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula119.json'

tarefa = ler([], CAMINHO_ARQUIVO)
tarefa_refazer = []
    
while True:
    print('Comandos: listar, desfazer e refazer')
    desejo = input('Digite uma tarefa ou comando: ')
    match(desejo):
        case 'listar':
            os.system('cls')
            print(listar(tarefa))
        case 'desfazer':
            os.system('cls')
            print(desfazer(tarefa, tarefa_refazer))
        case 'refazer':
            os.system('cls')
            print(refazer(tarefa, tarefa_refazer))
        case _:
            os.system('cls')
            print(adicionar(tarefa, desejo))
    salvar(tarefa, CAMINHO_ARQUIVO)