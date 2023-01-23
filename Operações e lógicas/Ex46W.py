r=()
while(r!="N"):
    p=0
    p2=0
    #Solicita n valores
    n=int(input("Digite quantos valores(positivos e menor que 20) seram solicitados: "))
    while(n<=0 or n>=20):
        print("Valor invalido!")
        n=int(input("Digite um valor positivo menor que 20: "))
    i=1
    while(i<=n):
        num=int(input(f"Digite um valor(n{i}) : "))
        #Verifica o maior numero.
        if(i==1):
            a=num
        elif(num>a):
            a=num
        #Faz a soma.
        if(i==1):
            b=num
        else:
            b=b+num
        #Verifica o menor numero.
        if(i==1):
            c=num
        elif(num<c):
            c=num
        #Verifica porcentagem de numeros positivos.
        if(num>0):
            p=p+1
        x=(p*100)/n
        #Verifica porcentagem de numeros negativos.
        if(num<0):
            p2=p2+1
        x2=(p2*100)/n
        i=i+1
    print("O maior valor é:",a,"\nO menor valor é:",c,"\nA soma dos valores é:",b,"\nA media aritimetica é:",b/10,"\nPorcentagem de valores positivos é:",x,"\nPorcentagem de valores negativos:",x2)
    r=input("Deseja uma nova execução? (S) ou (N):")
    while((r!="S")and (r!="N")):
        print("Invalido! Apenas (S) ou (N).")
        r=input("Deseja uma nova execução? (S) ou (N):")