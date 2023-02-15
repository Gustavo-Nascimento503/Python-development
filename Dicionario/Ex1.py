dados = []

while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    profissao = input("Digite a sua profissão: ")
    salario = float(input("Digite o salário: "))

    possui_conta = input("Tem conta? s/n: ").lower() == "s"

    conta = {}
    if possui_conta:
        conta["banco"] = input("Digite o banco: ")
        conta["agencia"] = input("Digite a agência: ")
        conta["numero"] = input("Digite o número da conta: ")

    cliente = {
        "nome": nome, 
        "idade": idade, 
        "salario": salario, 
        "profissao": profissao, 
        "conta": conta
    }

    dados.append(cliente)

    continuar = input("Deseja continuar? (S/N) ").upper()
    if continuar == "N":
        break

for cliente in dados:
    print(f"Nome: {cliente['nome']} | Idade: {cliente['idade']} | Salário: {cliente['salario']} | profissão: {cliente['profissao']}")
    if cliente['conta']:
        print("Conta:")
        print(f"Banco: {cliente['conta']['banco']} | Agência: {cliente['conta']['agencia']} | Número: {cliente['conta']['numero']}")
