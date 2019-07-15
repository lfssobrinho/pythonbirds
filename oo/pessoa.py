class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    gabriel = Pessoa(nome= 'Gabriel')
    layla = Pessoa(nome= 'Layla')
    laecio = Pessoa(gabriel, nome= 'Laecio', idade= 36)
    print(Pessoa.cumprimentar(laecio))
    print(id(laecio))
    print(laecio.cumprimentar())
    print(laecio.nome)
    print(laecio.idade)
    for filho in laecio.filhos:
        print(filho.nome)