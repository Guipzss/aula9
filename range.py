a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = 0
if a < b:
    for termo in range(a, b):
        soma += termo
    print(soma)
else:
    print("error")