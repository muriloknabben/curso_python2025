import json

from aula127_1 import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    p1 = Pessoa(**pessoas[1])
    p1 = Pessoa(**pessoas[2])