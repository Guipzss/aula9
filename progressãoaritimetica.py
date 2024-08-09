a = int(input("primeiro termo: "))
b = int(input("quantidade de termos:"))
c = int(input("razão:"))
ulttermo = a + (b-1) * c
for termo in range(a, ulttermo+1, c):
    print(termo)
print("Finalizado")
