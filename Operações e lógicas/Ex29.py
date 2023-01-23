v1 = float(input('digite o primeiro valor: '))
v2 = float(input('digite o segundo valor: '))
v3 = float(input('digite o terceiro valor: '))

if (v1 < v2 < v3):
    print(v1, v2, v3)

elif(v1 < v3 < v2):
    print(v2, v1, v1)

elif(v2 < v1 < v3):
    print(v2, v1, v3)

elif(v2 < v3 < v1):
    print(v2, v3, v1)

elif(v3 < v1 < v2):
    print(v3, v1, v2)
else:
    print(v3, v2, v1)


    # FORMA ALTERNATIVA#

    #for c in range(0,3):

    #n =int(input("digite um valor: "))
    #if c == 0 or n > lista[-1]:
        #lista.append(n)
    #else:
        #pos = 0
        #while pos < len(lista):
            #if n <= lista[pos]:
            # lista.insert(pos, n)
             #break
            #pos +=1
#print("-=" * 30)
#print(f"os valores diogitaos em ordem foram a çista{lista}")