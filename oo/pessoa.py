class Pessoa:
    def __init__(self, nome=None, idade=0):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Laecio', 36)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)