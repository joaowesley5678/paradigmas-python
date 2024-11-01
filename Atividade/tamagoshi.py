class Tamagoshi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, fome):
        self.fome = fome

    def alterar_saude(self, saude):
        self.saude = saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retorna_nome(self):
        return self.nome

    def retorna_fome(self):
        return self.fome

    def retorna_saude(self):
        return self.saude

    def retorna_idade(self):
        return self.idade

    def imprimir(self):
        print(f"Nome: {self.nome}\nFome: {self.fome}\nSaude: {self.saude}\nIdade: {self.idade}")


t1 = Tamagoshi("dudu", False, True, 0)

t2 = Tamagoshi("bilu", True, True, 1)

t1.alterar_nome("dede")
t1.alterar_saude(False)
t1.alterar_fome(True)
t1.alterar_idade(5)
t1.imprimir()

t2.alterar_nome("bili")
t2.alterar_saude(False)
t2.alterar_fome(False)
t2.alterar_idade(10)
t2.imprimir()
