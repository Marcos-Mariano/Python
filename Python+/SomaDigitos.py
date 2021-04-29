n = int(input("Digite o valor de n: "))
soma=0
while  n > 0:
    
    rest = n % 10
    n = n // 10
    soma = rest + soma

print(soma)
