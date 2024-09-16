import time
### Declaração de onstantes
VALOR_LIMITE  = 500
LIMITE_SAQUES = 3
AGENCIA       = '0001'

def menu():
    return """
        =========================
            MENU PRINCIPAL
        =========================
        [ D  ] Depositar
        [ S  ] Sacar
        [ E  ] Extrato
        [ CU ] Criar Usuários
        [ CC ] Criar Conta
        [ LC ] Listar Contas
        [ Q  ] Sair
        =========================
    => """

def depositar(saldo, extrato, /):
    while True:
        valor = input("Informe o valor a ser depositado: ")
        if valor.lower() == 'q':
            return saldo, extrato
        try:
            valor = float(valor)
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print( 'Valordepositado com sucesso!' )
                time.sleep(2)
                return saldo, extrato
        except:
            print("Operação falhou! O valor informado é inválido. (Insira o valor 'Q' Caso queira voltar ao Menu Principal)")
            time.sleep(2)

def sacar(*, saldo, extrato, num_saques):
    while True:
        if saldo <= 0.0:
            print("Desculpe, sem saldo em conta. Consulte o menu de extrato!")   
            time.sleep(2)  
            return saldo, extrato, num_saques
        elif LIMITE_SAQUES == num_saques:
            print("Número máximo de saques excedido!")
            time.sleep(2)
            return saldo, extrato, num_saques

        

        valor = input("Informe o valor do saque: ")

        if valor.lower() == 'q':
            return saldo, extrato, num_saques
        
        try:
            valor = float(valor)
            if valor > VALOR_LIMITE:
                print("Operação falhou! O valor do saque excede o limite.(Insira o valor 'Q' Caso queira voltar ao Menu Principal)")
                time.sleep(2)                
            elif valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.(Insira o valor 'Q' Caso queira voltar ao Menu Principal)")
                time.sleep(2)

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                num_saques += 1
                print( 'Operação realizada com sucesso!' )
                time.sleep(2)
                return saldo, extrato, num_saques
        except:
            print("Operação falhou! O valor informado é inválido.(Insira o valor 'Q' Caso queira voltar ao Menu Principal)")
            time.sleep(2)

def exibir_extrato(saldo,/,*, extrato):
    print("\n========== EXTRATO BANCÁRIO ==========")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print("Movimentações:")
        print(extrato)
    print("\n---------------------------------------")
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("=======================================\n")
    time.sleep(2)

def valida_usuario( cpf, usuarios ):
    usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario[0] if usuario else None

def valida_cpf():
    while True:
        cpf = input( 'Informe o CPF (Somente números!!!)' )
        if len( cpf ) == 11 and not cpf.isalpha():
            return cpf
        else:
            print( 'CPF Inválido!' )
            time.sleep(1.5)
        
def criar_usuario(usuarios):
    #Validação extremamente simples e rudimentar quanto à validade do CPF
    cpf = valida_cpf()

    usuario = valida_usuario( cpf, usuarios )

    if usuario:
        print( 'Já existe um usuário cadastrado com esse CPF!' )
        time.sleep( 1.5 )
        return None
    else:
        nome          = input( 'Informe o nome completo: ' )
        dt_nascimento = input( 'Informe a data de nascimento (dd-mm-aaaa): ' ) 
        endereco      = input( 'Informe o endereço: ' )  

        usuarios.append( {'nome':nome, 'dt_nascimento':dt_nascimento, 'cpf':cpf, 'endereco':endereco} )
        print( 'Usuário criado com sucesso!' )
        time.sleep( 1.5 )
        return None

def criar_conta( agencia, numero_conta, usuarios ):
    cpf = valida_cpf()
    usuario = valida_usuario( cpf, usuarios )

    if usuario:
        print( 'Usuário criado com sucesso!' )
        time.sleep(1.5)
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    else:
        print('Usuário não encontrado!')
        time.sleep(1.5)

def exibir_contas( contas ):
    if contas == []:
        print( 'Nenhum usuário cadastrado!' )
        time.sleep(1.5)
    else:        
        for conta in contas:        
            print( f'''
            =========================
            Agência: {conta['agencia']}
            Conta: {conta['numero_conta']}    
            Titular: {conta['usuario']['nome']}
            =========================
            ''' )
        time.sleep(2)

def main():
    #Declaração de variáveis
    saldo      = 0.0
    extrato    = ""
    num_saques = 0
    usuarios   = []
    contas     = []

    while True:
        opcao = input(menu())

        if opcao.lower() == "d":
            saldo, extrato = depositar( saldo, extrato )

        elif opcao.lower() == "s":
            saldo, extrato, num_saques = sacar( saldo=saldo, extrato=extrato, num_saques=num_saques )

        elif opcao.lower() == "e":
            exibir_extrato( saldo, extrato=extrato )
        elif opcao.lower() == 'cu':
            criar_usuario( usuarios )  
        elif opcao.lower() == 'cc':
            numero_conta = len(contas) + 1
            conta = criar_conta( AGENCIA, numero_conta, usuarios )
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            exibir_contas( contas )
        elif opcao.lower() == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    


main()    

    