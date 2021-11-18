# Cria a classe Aluno e define seus atributos, define método para classificar e o método __str__ para retornar as informações
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def classifica(self):
        if self.idade < 6:
            return "Educação Infantil"
        elif self.idade < 11:
            return "Ensino Fundamental I"
        elif self.idade < 15:
            return "Ensino Fundamental II"
        else: 
            return "Ensino Médio"

    def __str__(self):
        return "Aluno(a) "+ self.nome\
            + " tem " + str(self.idade)\
            + " anos e está no " + self.classifica()

#Cria loop até que a entrada seja 0, qualquer valor diferente irá reiniciar 
while True:
    nome = input("Nome da criança: ")
    idade = int(input("Qual idade? "))
    a1 = Aluno(nome, idade)
    print(a1)
    loop = input("Deseja continuar? 0-Não 1-Sim ")
    if int(loop) == 0: break
