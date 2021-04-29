opc = 0
n = 0
m = 0
y = 0
z = 1
pl1 = 0
pl2 = 0

def funcVal(opc,z):
    while opc == 1 or opc == 2:
        if opc == 1:
            print ("\nVoce escolheu uma partida isolada!\n")
            return partida(n,m)
        else: 
            if opc == 2:
                print("\nVoce escolheu um campeonato!\n")
                return campeonato(z,pl1,pl2)

    while opc != 1 and opc != 2:
        return funcNot(opc)

def funcNot(opc):
    print("Opção inválida...")
    opc = int(input("\nEscolha uma opção válida: "))
    return funcVal(opc,z)

def computador_escolhe_jogada(n,m):
    pcjoga = 1

    while pcjoga !=m:
        if (n - pcjoga) % (m+1) == 0:
            return pcjoga

        else:
            pcjoga = pcjoga + 1

    return pcjoga
                    
def usuario_escolhe_jogada(n,m):
    x = int(input("\nQuantas peças você vai tirar? "))
    if 1 <= x <= m:
        return x
                      
    else:
        print("\nOops! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n,m)

def campeonato(z,pl1,pl2):
    while z <= 3:
        print("**** Rodada", z, "****\n")
        print (partida(n,m))
        z = z + 1
        pl1 = pl1 + 1
    while z == 4:
        print("Placar: Você", pl2, "X", pl1, "Computador")
        exit()
        

def partida(n,m):
    pc = False
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if m > n:
        pc = False
        print("\nO número de peças tem de ser maior do que o de limites!\n")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
    else:
        if n >= m:
            resto = n % (m+1)

            if resto == 0:
                print("\nVoce começa!")
                #return usuario_escolhe_jogada(n,m)

            else:
                print("\nComputador começa!")
                #return computador_escolhe_jogada(n,m)
                pc = True
    while n > 0:
        if pc:
            pcjoga = computador_escolhe_jogada(n, m)
            n = n - pcjoga
            if pcjoga == 1:
                print("\nO computador tirou uma peça")
            else:
                print("\nO computador tirou", pcjoga,"peças")
            pc = False
        else:
            x = usuario_escolhe_jogada(n, m)
            n = n  - x
            if x == 1:
                print("\nVocê tirou uma peça")
            else:
                print("\nVocê tirou", x, "peças")
            pc = True
        if n == 1:
            print ("\nAgora resta apenas uma peça no tabuleiro.")
        else:
            if n !=0:
                print ("Agora restam", n, "peças no tabuleiro.")

    print("Fim do jogo! O computador ganhou!") 

print("\nBem-vindo ao jogo do NIM! Escolha:\n")

print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
opc = int(input())
print(funcVal(opc,z))
