# funcao para instruções inicais
def posicoes():
    print("____HOTEL DOS ANIMAIS____")
    print("Cada número abaixo corresponde a um quarto conforme o próprio diagrama")
    print("[1 2 3 4]")
    print("[5 6 7 8]\n")
    print("Quartos marcados com * estão ocupados")
    print("Quartos marcados com _ estão disponíveis")
    print("Cada letra possui uma representação:")
    print("GATO(G) - CÃO(C) - RATO(R) - OSSO(O) - QUEIJO(Q)\n")

#funcao para mensagens de erro e finalização
def msgPerdeu():
    print("Você perdeu!! Tente novamente.")

def msgVitoria():
    print("Você ganhou!! Considere-se um excelente gestor de hotel para animais.")

#funcoes para as fases. Gabarito para conferencia de respostas, estatus inicial da fase e alocação dos hospedes. Retorno em lógica negativa onde o acerto retorna falso e o jogo continua
def fase01():
    valida = ["*", "*", "G", "G", "R", "R", "*", "*"]
    fase = ["*", "*", "_", "G", "R", "_", "*", "*"]
    hospedes = ("Rato", "Gato")
    print('Bem vindo a fase 01!')
    print('Você precisa escolher um quarto para: \n-Rato(R)\n-Gato(G)')
    print('Quartos disponíveis: 3 e 6')
    print(fase[:4])
    print(fase[4:])
    for h in hospedes:
        quarto = int(input("Qual quarto para o " + h +"? "))
        fase[quarto-1] = h[0]
    
    return False if valida == fase else True 

def fase02():
    valida = ["O", "*", "*", "*", "*", "C", "C", "C"]
    fase = ["_", "*", "*", "*", "*", "C", "_", "_"]
    hospedes = ("Cão", "Cão", "Osso")
    print('\nBem vindo a fase 02!')
    print('Você precisa escolher um quarto para: \n-Cão(C)\n-Cão(C)\n-Osso(O)')
    print('Quartos disponíveis: 1, 7 e 8')
    print(fase[:4])
    print(fase[4:])
    for h in hospedes:
        quarto = int(input("Qual quarto para o " + h +"? "))
        fase[quarto-1] = h[0]
    
    return False if valida == fase else True 

def fase03():
    valida = ["R", "*", "*", "*", "O", "G", "G", "*"]
    fase = ["_", "*", "*", "*", "_", "G", "_", "*"]
    hospedes = ("Gato", "Rato", "Osso")
    print('\nBem vindo a fase 03!')
    print('Você precisa escolher um quarto para: \n-Gato(G)\n-Rato(R)\n-Osso(O)')
    print('Quartos disponíveis: 1, 5 e 7')
    print(fase[:4])
    print(fase[4:])
    for h in hospedes:
        quarto = int(input("Qual quarto para o " + h +"? "))
        fase[quarto-1] = h[0]
    
    return False if valida == fase else True 


def fase04():
    valida = ["Q", "O", "Q", "*", "*", "R", "*", "*"]
    fase = ["_", "_", "_", "*", "*", "R", "*", "*"]
    hospedes = ("Queijo", "Queijo", "Osso")
    print('\nBem vindo a fase 04!')
    print('Você precisa escolher um quarto para: \n-Queijo(Q)\n-Queijo(Q)\n-Osso(O)')
    print('Quartos disponíveis: 1, 2 e 3')
    print(fase[:4])
    print(fase[4:])
    for h in hospedes:
        quarto = int(input("Qual quarto para o " + h +"? "))
        fase[quarto-1] = h[0]
    
    return False if valida == fase else True 

#chamada das funcoes até que um retorno True execute a interrupção do loop
posicoes()
while True:
    fase=fase01()
    if fase:
        msgPerdeu()
        break
    fase=fase02()
    if fase:
        msgPerdeu()
        break
    fase=fase03()
    if fase:
        msgPerdeu()
        break
    fase=fase04()
    if fase:
        msgPerdeu()
        break
    else:
        msgVitoria()
        break
