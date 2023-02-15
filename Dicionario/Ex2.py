products = []

while True:
    product = {}
    product['name'] = input("Digite o nome do produto: ")
    product['price'] = float(input("Digite o preço do produto: "))
    product['quantity'] = int(input("Digite a quantidade do produto: "))
    product['stores'] = []

    while True:
        store = {}
        store['name'] = input("Digite o nome da loja (deixe em branco para terminar): ")
        if store['name'] == '':
            break
        store['city'] = input("Digite a cidade da loja: ")
        product['stores'].append(store)
        
    products.append(product)
    
    another = input("Cadastrar outro produto? (S/N) ")
    if another.upper() != 'S':
        break

print("\nPRODUTOS CADASTRADOS:")
for product in products:
    print(f"Nome: {product['name']}")
    print(f"Preço: R${product['price']:.2f}")
    print(f"Quantidade: {product['quantity']}")
    if product['stores']:
        print("Lojas:")
        for store in product['stores']:
            print(f"\tNome: {store['name']}")
            print(f"\tCidade: {store['city']}")
    print()
