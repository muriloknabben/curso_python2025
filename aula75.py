# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicate(num):
    def multiplicator(mult):
        return num * mult
    return multiplicator

number = multiplicate(4)

for n in [2, 3, 4]:
    print(number(n))