from Cliente import Cliente
from ContaBancaria import ContaBancaria

clientes = []

for i in range(5):
    if i != 0:
        print("Digite os dados do próximo cliente")

    id = i + 1
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    email = input("Digite o email do cliente: ")
    cliente = Cliente(id, nome, idade, email)
    resposta = input("O cliente tem conta bancária? (s/n) ")[0].lower()
    if resposta == "s":
        agencia = input("Digite a agência da conta bancária: ")
        numero = input("Digite o número da conta bancária: ")
        saldo = float(input("Digite o saldo da conta bancária: "))
        conta_bancaria = ContaBancaria(agencia, numero, saldo)
        cliente.adicionar_conta_bancaria(conta_bancaria)
    clientes.append(cliente)

# Exibir todos os clientes e suas respectivas contas bancárias, se houver
for cliente in clientes:
    print("Id: ", cliente.id)
    print("Nome: ", cliente.nome)
    print("Idade: ", cliente.idade)
    print("Email: ", cliente.email)
    conta_bancaria = cliente.conta_bancaria
    if conta_bancaria is not None:
        print("Agência: ", conta_bancaria.agencia)
        print("Número: ", conta_bancaria.numero)
        print("Saldo: ", conta_bancaria.saldo)
    else:
        print("Cliente não possui conta bancária.")
    print()