menu = """
=========================
       MENU PRINCIPAL
=========================
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
=========================
=> """
LIMITE_SAQUES = 3
VALOR_LIMITE = 500

saldo = 0
extrato = ""
num_saques = 0

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        while True:
            valor = input("Informe o valor a ser depositado: ")
            if valor.lower() == 'q':
                break
            try:
                valor = float( valor )
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f}\n"
                    break
            except:
                print("Operação falhou! O valor informado é inválido. (Insira o valor 'Q' Caso queira voltar ao Menu Principal)")

    elif opcao.lower() == "s":
        while True:
            valor = input("Informe o valor do saque: ")
            if valor.lower() == 'q':
                break
            try:   
                valor = float(valor)
                

                if valor > VALOR_LIMITE:
                    print("Operação falhou! O valor do saque excede o limite.(Insira o valor 'Q' Caso queira voltar ao Menu Principal)")

                elif num_saques >= LIMITE_SAQUES:
                    print("Número máximo de saques excedido!")
                    break
                    
                elif valor > saldo:
                    print("Operação falhou! Você não tem saldo suficiente.(Insira o valor 'Q' Caso queira voltar ao Menu Principal)")                    

                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    num_saques += 1
                    break

            except:
                print("Operação falhou! O valor informado é inválido.(Insira o valor 'Q' Caso queira voltar ao Menu Principal)")

    elif opcao.lower() == "e":
        print("\n========== EXTRATO BANCÁRIO ==========")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            print("Movimentações:")
            print(extrato)
            
        print("\n---------------------------------------")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("=======================================\n")


    elif opcao.lower() == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")