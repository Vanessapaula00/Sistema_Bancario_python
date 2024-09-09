from datetime import datetime

menu = """
Bem-vindo ao sistema bancário!

[d] Depositar
[s] Sacar
[e] Extrato
[c] Configurar limite de saque
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))

            if valor > 0:
                saldo += valor
                extrato += f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Por favor, insira um valor válido para o depósito.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
            elif excedeu_saques:
                print(f"Operação falhou! Número máximo de saques ({LIMITE_SAQUES}) excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Por favor, insira um valor válido para o saque.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "c":
        try:
            novo_limite = float(input(f"Informe o novo limite de saque (atual: R$ {limite:.2f}): R$ "))
            if novo_limite > 0:
                limite = novo_limite
                print(f"Novo limite de saque definido para R$ {limite:.2f}")
            else:
                print("Operação falhou! O limite informado é inválido.")
        except ValueError:
            print("Por favor, insira um valor válido para o limite de saque.")

    elif opcao == "q":
        print("Obrigado por utilizar o sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")
