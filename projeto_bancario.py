menu = "Informe uma opcao: \n[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Sair\n"

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3

while True:  

    opcao= input(menu)

    if opcao == "1":
        valor = float (input("Informe o valor do Depósito: "))

        if valor >= 0:
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n" 
            print("Depósito realizado com sucesso \n")

        else:
            print("operação falou! O valor informado é inválido \n")

    elif opcao == "2":
        valor = float (input("Informe a quantia do Saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= limite_saque   

        if excedeu_saldo:
            print("Saldo insulficiente")

        elif excedeu_limite:
            print("Limite de  Saque excedido")

        elif excedeu_saques:
            print("Número máximo de Saque excedido")

        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f"Saque: R$ {valor:.2f}\n" 
            numero_saque = numero_saque + 1 
            print("Saque realizado com sucesso")

        else:
            print("Operação falhou! O valor informado é inválido.")
     
    elif opcao == "3":
            print("Não foram realizadas movimentações" if not extrato else extrato)
            print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada: ")