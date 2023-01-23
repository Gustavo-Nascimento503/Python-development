manha=[]
tarde=[]
noite=[]
lotacao_manha = 0
lotacao_tarde = 0
lotacao_noite = 0
retornar="s"
 
print("Reservas do Show do CBJR \o/")
 
fileiras = int(input('Quantas fileiras a casa de show terá? '))
cadeiras = int(input('Quantas cadeiras cada fileira da casa de show terá? '))
 
for i in range(0, fileiras, 1):
    manha.append([])
    tarde.append([])
    noite.append([])
 
for l in range(0, fileiras, 1):
    for c in range(0, cadeiras, 1):    
        manha[l].append("vazio")
        tarde[l].append("vazio")
        noite[l].append("vazio")
 
while(retornar=="s"):
    nome = input("Digite o seu nome: ")
    sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))
    fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
    cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1
 
    while((sessao == 1) and (lotacao_manha >= ((fileiras * cadeiras)*0.80) ) ):
        print('Sessao lotada, escolha outra sessão!')
        sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))
 
    while((sessao == 2) and (lotacao_tarde >= ((fileiras * cadeiras)*0.80) ) ):
        print('Sessao lotada, escolha outra sessão!')
        sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))
 
    while((sessao == 3) and (lotacao_noite >= ((fileiras * cadeiras)*0.80) ) ):
        print('Sessao lotada, escolha outra sessão!')
        sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))
 
    if (sessao == 1):
        while (manha[fileira][cadeira] != "vazio"):
            print("Esse assento já está reservado!")
            fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
            cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1
 
        manha[fileira][cadeira] = nome
        lotacao_manha = lotacao_manha + 1
    elif (sessao == 2):
        while (tarde[fileira][cadeira] != "vazio"):
            print("Esse assento já está reservado!")
            fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
            cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1
 
        tarde[fileira][cadeira] = nome
        lotacao_tarde = lotacao_tarde + 1
    else:
        while (noite[fileira][cadeira] != "vazio"):
            print("Esse assento já está reservado!")
            fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
            cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1
        noite[fileira][cadeira] = nome
        lotacao_noite = lotacao_noite + 1
 
    print("Reserva realizada com sucesso!")
   
    if ( (lotacao_manha >= ((fileiras * cadeiras)*0.80) ) and
         (lotacao_tarde >= ((fileiras * cadeiras)*0.80) ) and
         (lotacao_noite >= ((fileiras * cadeiras)*0.80) ) ):
        print("Todas as sessões estão lotadas!")
        break
    else:
        retornar = input("Deseja realizar mais alguma reserva? (S/N)")
 
print("Mapa das reservas do show separados por período:")
 
print("Reservas da Manhã")
for i in range(0, fileiras, 1):
    print(manha[i])
 
print("Reservas da Tarde")
for i in range(0, fileiras, 1):
    print(tarde[i])
 
print("Reservas da Noite")
for i in range(0, fileiras, 1):
    print(noite[i])
