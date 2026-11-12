def greet():
    print("Olá Eduardo")
    
greet()

# Python não suporta sobrecarga *
def greet(name):
    print(f"Olá, {name}!")
    
greet("Eduardo")
greet("Carlos")

# Exercício 1

def calculate_average(n1 , n2):
    print((n1+n2)/2)

calculate_average(8,10)
calculate_average(8,9)
calculate_average(8,4)

# Exercício 2

def calculate_square(n):
    return n**2
    
n = calculate_square(10)
print(f"Resultado: {n}")
    
# Exercício 3

def check_age(age):
    if age >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
print(check_age(15))
print(check_age(20))

# Exercício 4

name = "Eduardo"

def greet():
    message = "Olá, " + name 
    print(message)
    
greet()

# Exercício 5

def calculate():
    number = 10
    return number * 2

print(calculate())
#print(number) # Não pode ser acessada pois é variável local

# Exercício 6

def calculate_sum(n1, n2, n3):
    return n1 + n2 + n3

print(calculate_sum(10, 20, 30))

# Exercício 7

def calculate_sum(*args):
    i = 0
    sum = 0
    
    while i < len(args):
        sum += args[i]
        i += 1
        
    return sum

print(calculate_sum(1, 1, 2, 2))
print(calculate_sum(1, 110))
print(calculate_sum(1, 34 ,2))
    
# Exercício 8

def show_user(**kwargs):
    i = 0
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
show_user(name = "Eduardo", age = 18, course = "Software Engineer")

# Exercício 9

def calculate_average(*args):
    total = 0
    for number in args:
        total+= number
        
    return total/len(args)

print(calculate_average(8, 10))
print(calculate_average(7, 8, 9))
print(calculate_average(10, 10, 10, 10))
        
# Exercício 10

def calculate_cube(n):
    return n**3
