# Exercício 1 - Contagem
limit = int(input("Digite um número: "))

for number in range(1, limit + 1):
    print(number)
    
# Exercício 2 - Soma com for

n = int(input("Digite um número: "))
total = 0
for number in range (1, n + 1):
    total += number
    
print(total)

# Exercício 3 — Agora com while

n = int(input("Digite um número: "))
count = 1
total = 0
while count <= n:
    total+=count
    count += 1
    
print(total)

# Exercício 4 — Tabuada

n = int(input("Digite um número: "))

for mult in range(1, 11):
    print(f"{mult} x {n} = {mult * n}")