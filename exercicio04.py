from random import seed
from random import randint
#funcao para gerar vouchers conforme a quantidade requerida
def gerarVouchers(quantidade):
    vouchers=[]
    seed(60)
    for i in range (1,quantidade):
        vouchers.append(randint(100, 400))
    return vouchers

#funcao para criar nova inscricao retornando dados no tipo dicionário
def novaInscricao(voucher):
    inscricao = {'voucher': '', 'nome': '', 'email': '', 'telefone': '', 'curso': ''}
    inscricao['voucher'] = voucher
    inscricao['nome'] = input('Digite o nome: ')
    inscricao['email'] = input('Digite o email: ')
    inscricao['telefone'] = input('Digite o telefone: ')
    inscricao['curso'] = input('Digite o curso: ')
    return inscricao

#funcao para exibir as informações de cada um dos elementos do parametro
def listar(inscricoes):
    print("----------------[ LISTA DE INSCRITOS ]----------------")
    for i in inscricoes:
        print("Voucher: ", i['voucher'])
        print("Nome: ", i['nome'])
        print("Email: ", i['email'])
        print("Telefone: ", i['telefone'])
        print("Curso: ", i['curso'])
        print("--------------------------------")

#funcao para exibir as opcoes de menu e retornar a escolha feita
def menu():
    print('##############[ MENU ]##############')
    print('Entre com uma função')
    print('[1] Nova inscrição')
    print('[2] Visualizar inscrições')
    print('[0] Encerrar')
    opcao = input("Opção escolhida: ")
    return int(opcao)

vouchers = gerarVouchers(40)
inscricoes = []
while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        inscricoes.append(novaInscricao(vouchers.pop()))
    elif opcao == 2:
        if len(inscricoes) == 0: print("Nenhuma inscrição cadastrada")
        else: listar(inscricoes)
    else:
        print("Escolha uma opção válida indicada pelo numero da função")

