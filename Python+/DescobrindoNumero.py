import os, code
import random

def func(x):
    return x*2 + 2*x

ops=0
x = 1

while ops !=2:
    print("\n     ----------Leitor de Mente----------\n")
    print("\n     PASSO 1: PENSE EM UM NÚMERO...")
    ops = int(input("\n     Clique 1 para continuar ou 2 para encerrar: "))
    if ops == 1:
        print("\n     PASSO 2: MULTIPLIQUE POR", x, "...")
        ops=int(input("\n     Clique 1 para continuar ou 2 para encerrar: "))
    if ops == 1:
        print("\n     PASSO 3: SOME O RESULTADO COM", func(x), "...")
        ops=int(input("\n     Clique 1 para continuar ou 2 para encerrar: "))
    if ops == 1:
        print("\n     PASSO 4: DIVIDA POR", x, "...")
        ops=int(input("\n     Clique 1 para continuar ou 2 para encerrar: "))
    if ops == 1:
        print("\n     PASSO 5: PEGUE O RESULTADO E SUBTRAIA O NÚMERO QUE VOCÊ PENSOU...")
        ops=int(input("\n     Clique 1 para continuar ou 2 para encerrar: "))
    if ops == 1:
        y = random.randint(1,200)
        print("\n     PASSO 6: SOME O RESULTADO COM", y, "...")
        ops=int(input("\n     Clique 1 para continuar ou 2 para encerrar: "))
    if ops == 1:
        ops=int(input("\n     ......VAMOS VER SE EU SEI O RESULTADO?\n\n     Clique 1 para continuar ou 2 para encerrar: "))
    if ops == 1:
        print("\n     ......O RESULTADO É.....", (func(x) /(x)) + y)
        ops=int(input("\n     Deseja realizar outro teste (1-Sim/2-Não): "))
    if ops == 1:
        os.system ("cls")
        x = random.randint(1, 15)                    

                            
while ops == 2:
    print("\nSaindo.....")
    os.system ("cls")
    exit()

