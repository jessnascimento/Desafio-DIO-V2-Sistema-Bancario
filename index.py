import textwrap

def menu():
    menu = """"\n
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova conta
    [lc] \tListar contas
    [nu] \tNovo usuario
    [q] \tSair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0 :
        saldo += valor
        extrato += f"Deposito: \t R$ {valor:.2f}\n"
        print("\n--- Deposito realizado com sucesso! ---")
    else:
          print(f"---Operação falhou! O valor informado é invalido ---")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("--- Operação falhou! Saque maior que o saldo disponivel ---")

    elif excedeu_limite:
        print("--- Operação falhou! Valor acima do limite de saque ---")
        
    elif excedeu_limite_saques:
        print("--- Operação falhou! Numero máximo de saques atingido ---")

    elif valor>0:
        saldo-= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"--- Saque realizado com sucesso! ---")
    else:
        print("--- Operação falhou! Valor invalido ---")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("--- Extrato ---")
    print(f"-----Extrato-----")
    print("Não foi realizado movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print(f"-----------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros) :")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Já existe um usuarios com esse CPF")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa) :")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado) :")

    usuarios.append({"nome" : nome, "data_nascimento" : data_nascimento, "cpf" : cpf, "endereco" : endereco})
    print("--- Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario :")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "usuario" : usuario}
    print("\nUsuario não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: \t {conta['agencia']}
            C/C: \t\t {conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do deposito:"))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque:"))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                limite_saques = LIMITE_SAQUES,
                numero_saques = numero_saques
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção invalida!")

main()