print("\n------Calculando as Raizes da Equação------")

new=0

import math

def delta(a,b,c):
    return ((b**2)-(4*a*c))

def raiz1(a,b):
    return ((-b)/(2*a))

def raiz2(a,b):
    return (((-b) + math.sqrt(delta(a,b,c)))/(2*a))

def raiz3(a,b):
    return (((-b) - math.sqrt(delta(a,b,c)))/(2*a))

while new != 2:

    print("\nBhaskara: a X^2 + b X + c = 0\n")

    a=int(input("Digite o termo 'a' da equação: "))
    b=int(input("Digite o termo 'b' da equação: "))
    c=int(input("Digite o termo 'c' da equação: "))


    if a==0 or delta(a,b,c) < 0:
        print("\nEssa equação não é de segundo grau ou não possui raizes reias!!!\n")
    
        new=int(input("\nDeseja calcular as raizes de outra equação? (1 - Sim / 2 - Não): "))
    
    else:
        if delta(a,b,c) == 0:
            print("\nA raiz desta equação é:", raiz1(a,b))

            new=int(input("\nDeseja calcular as raizes de outra equação? (1 - Sim / 2 - Não): "))
        else:
           # if delta > 0:
               
            print("\nAs raizes da equação são", raiz2(a,b), "e", raiz3(a,b), ".")

            new=int(input("\nDeseja calcular as raizes de outra equação? (1 - Sim / 2 - Não): "))
while new == 2:
    print("\nSaindo.....")
    exit()
