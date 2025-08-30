nome = 'Murilo'
altura = 1.80
peso = 90

imc = peso / altura ** 2

print(f'O peso de {nome} é: {peso} \nSua altura é: {altura:.2f} \nE seu IMC é: {imc}')
# :.xf serve para deixar com um numero x de casas decimais
# também pode ser usado :,.2f para o numero sair disso -> 100000 para isso -> 100,000.00