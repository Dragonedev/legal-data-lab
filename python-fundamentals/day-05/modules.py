# Exercício 10

from functions import calculate_cube

print(calculate_cube(3))

# Exercício 11

from math import sqrt

print(sqrt(144))

# Exercício 12

from random import randint

number = randint(1, 100)
print(number)

# Exercício 13

from datetime import datetime

current_date = datetime.now()
print(current_date)

# Exercício 14

formatted_date = current_date.strftime("%d/%m/%Y")
formatted_time = current_date.strftime("%H:%M")

print(f"Data: {formatted_date}")
print(f"Hour: {formatted_time}")

# Exercício 15

random_number = randint(1,100)
current_date = datetime.now()
formatted_date = current_date.strftime("%d/%m/%Y")
print(f"Número sorteado: {random_number}")
print(f"Data atual: {formatted_date}")

# Exercício 16

def generate_report(name, *args):
    total = 0
    for n in args:
        total += n
        
    avg = total/len(args)
    
    random_number = randint(1, 100)
    current_date = datetime.now().strftime("%d/%m/%Y")
    return f"Aluno: {name} | Média: {avg} | Número de identificação: {random_number} | Data: {current_date}"

report = generate_report("Eduardo", 8, 9, 10)
print(report)
    