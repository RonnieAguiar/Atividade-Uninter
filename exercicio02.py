# Cria a classe Nome com atributo nome, define método de codificar e __str__ para retornar o nome e nome codificado
class Nome:
    def __init__ (self, nome):
        self.nome = nome

    def codifica(self):
        codificado = self.nome
        vogal = ("AEIOU")
        cod = ("@&!#*")
        for i in range(0, 5):
            codificado = codificado.replace(vogal[i], cod[i])
        return codificado

    def __str__(self):
        return self.nome+"\n"+self.codifica()
    

nome = input("Informe o nome: ").upper()
cod = Nome(nome)
print(cod)
