r=()
while(r!="N"):
    n=int(input("Digite um valor positivo: "))
    while(n<0):
        print("Valor invalido!")
        n=int(input("Digite um valor positivo: "))
    for i in range(n,0,-1):
        if(i==n):
            f=i
        else:
            f=f*i
    print(f"{n}!={f}")
    
    r=input("Deseja uma nova execução? (S) ou (N):")
    while((r!="S")and (r!="N")):
        print("Invalido! Apenas (S) ou (N).")
        r=input("Deseja uma nova execução? (S) ou (N):")