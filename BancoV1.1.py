def menu():
    menu = """\n
    ======== BOSS BANK ========
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair

    => """

    return input(menu)


def depositar(saldo, valor, extrato, /):

    if valor >0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso!===")
    else:
        print("\n--- A operação falhou! O valor solicitado é inválido. ---")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
    excedeu_saque = valor > limite 
    excedeu_limite = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n----- Falha na operação! Você não possui saldo o suficiente.!! -----")
    elif excedeu_saque:
        print("\n----- Falha na operação! O valor de saque solicitado excede o limite.!! -----")
    elif excedeu_limite:
        print("\n Falha na operação! Número máximo de saques excedido.!! -----")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n====== Saque realizado com Sucesso.! ======")

    else:
        print("\n ------ Falha na operação! O Valor informado é inválido.!! ------")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================")
        

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\t----- Já existe um usuário com esse CPF! -----")
        return
    
    nome = input("Digite seu Nome Completo: ")
    data_nascimento = input("Digite sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("===== Usuário criado com sucesso! =====")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n===== Conta criada com sucesso! =====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n----- Usuário não encontrado, fluxo de criação de conta encerrado! -----")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)
        

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
