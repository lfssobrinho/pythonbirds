
"""

    Exemplo:
    >>> #Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade()
    0

"""


class Carro:

    def __init__(self, direcao=None, motor=None):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        print(self.motor.velocidade)

    def acelelar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:

    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL : OESTE, OESTE : NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL : LESTE, OESTE : SUL
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0;

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)



if __name__ == '__main__':
    #Testando o motor
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    # Testando a direção
    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)


    carro = Carro(direcao=direcao, motor=motor)
    carro.calcular_velocidade()
    carro.motor.acelerar()
    carro.calcular_velocidade()
    carro.motor.acelerar()
    carro.calcular_velocidade()
    carro.frear()
    carro.calcular_velocidade()