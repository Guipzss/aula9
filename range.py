a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = 0
if a < b:
    for termo in range(a, b+1):
        soma += termo
    print(soma)
else:
    print("error")
