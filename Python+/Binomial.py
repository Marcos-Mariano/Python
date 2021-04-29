def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

#def fatorial(k):
#    fat = 1
#    while (k > 1):
#        fat = fat * k
#        k = k - 1
#    return fat

#def fatorial(z):
#    fat = 1
#    while ((z) > 1):
#        fat = fat * (z)
#        (z) = (z) - 1
#    return fat

def numero_binomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Fatorial para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Fatorial para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Fatorial para 5")
    else:
        print("Não funciona para 5")

n = int(input("Dígite um numero n: "))
k = int(input("Dígite um numero k: "))

print (numero_binomial(n, k))