n = int(input("Digite um número positivo: "))

def fator(n):
    fat = 1
    while  n > 1:
        fat = fat*n
        n = n - 1
    return fat

while n >= 0:
    print (fator(n))
    n = int(input("Digite um número positivo: "))