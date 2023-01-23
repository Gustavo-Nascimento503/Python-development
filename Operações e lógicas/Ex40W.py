
v = 20
n1 = 1
n2 = 1
n3 = 1
n4 = 3

print(f'1 : {n1}')
print(f'2 : {n2}')
print(f'3 : {n3}')

while (n4 <= 20):
    a = n1 + n2 + n3
    print(f'{n4} : {a}')
    n1 = n2
    n2 = n3
    n3 = a
    n4 = n4 + 1
