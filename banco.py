import os

nomes = []
saldo = []
conta = []

def limpar():
    os.system('cls')
    
def msn():
    print("Opção inválida")
    
def cadastro(numero, nome):  
    nomes.append(nome)
    conta.append(numero)
    saldo.append(0)    
    return "A conta foi cadastrada com sucesso"

def transferir():
    limpar()
    num_origem = int(input("Digite o número da conta de origem: "))
    if num_origem not in conta:
        return "Conta de origem não encontrada"
    num_destino = int(input("Digite o número da conta de destino: "))
    if num_destino not in conta:
        return "Conta de destino não encontrada"
    valor = int(input("Digite o valor a ser transferido: "))
    posicao_origem = conta.index(num_origem)
    posicao_destino = conta.index(num_destino)
    if saldo[posicao_origem] < valor:
        return "Saldo insuficiente para transferência"
    saldo[posicao_origem] -= valor
    saldo[posicao_destino] += valor
    return "Transferência realizada com sucesso!"
        
def sacar(num):
    limpar()
    if num in conta:
        valor = int(input("Digite o valor a ser sacado: "))
        if valor > 1000:
            return "O valor máximo permitido por saque é 1000"
        posicao = conta.index(num)
        if saldo[posicao] < valor:
            return "Saldo insuficiente para saque"
        saldo[posicao] -= valor
        return "Saque realizado com sucesso!"
    else:
        return "Conta Inexistente"

def depositar(num):
    limpar()
    if num in conta:
        valor = int(input("Digite o valor a ser depositado: "))
        posicao = conta.index(num)
        saldo[posicao] = (saldo[posicao]) + valor
        return "Deposito realizado com sucesso!"
    else:
        return "Conta Inexistente"

def pesquisar():  
    limpar()  
    print("Número\tNome\tSaldo")
    cont = 0
    while cont < len(nomes):
        print(conta[cont], "\t", nomes[cont], "\t", saldo[cont],"R$")
        cont += 1

    
def deletar(num):
    limpar()
    if num in conta:       
       posicao = conta.index(num)       
       conta.pop(posicao)
       nomes.pop(posicao)
       msn = "A conta foi removida com sucesso"
       return msn
    else:
        return  ("Não há nenhuma conta cadastrada com este numero")
    
op = 10

while op != 0:
    op = int(input("Banco Kaligula"
                   "\n 1 - Cadastrar uma nova conta "
                   "\n 2 - Pesquisar conta e verificar saldo "
                   "\n 3 - Delete uma conta "
                   "\n 4 - Transferencias  "
                   "\n 5 - Depositos "
                   "\n 6 - Saque "
                   "\n 0 - Feche o sistema "
                   "\nEscolha a opção: "))
    
    if op == 1:
        limpar()
        num = int(input("Digite o numero da nova conta: "))
        identificacao = input("Digite seu nome: ")
        print(cadastro(num, identificacao))
        
    elif op == 2:
        pesquisar()

    elif op == 3:
        valor = int(input("Digite o número da conta a ser deletada: "))        
        retorno = deletar(valor)   
        print(retorno)
        
    elif op == 4:  
        transferir()  
        
    elif op == 5:
        numero = int(input("Digite o numero da conta para prosseguir: "))    
        print(depositar(numero))
        
    elif op == 6:
        numero = int(input("Digite o numero da conta para prosseguir: "))    
        print(sacar(numero))
        
    elif op == 0:
        limpar()
        print("Sistema Encerrado")

    else:
        limpar()
        print("\nOpção invalida, tente novamente\n")