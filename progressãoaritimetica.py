a = int(input("primeiro termo: "))
b = int(input("quantidade de termos:"))
c = int(input("razão:"))
y = 0
for x in range(a, b+1, c):
    y += x
print(y)