# Exercício 1 - Calculadora

number1 =float(input("Digite um número: "))
number2 =float(input("Digite outro número: "))

print("Soma: ", number1 + number2)
print("Subtração: ", number1 - number2)
print("Multiplicação: ", number1 * number2)
print("Divisão: ", number1 / number2)

# Exercício 2 - Maioridade

age = int(input("Digite sua idade: "))

print("Maior de idade: ", age >= 18)
print("Menor de idade: ", age < 18)
print("Extamente 18 anos: ", age == 18)

# Exercício 3 - Operadores Lógicos

age = 20
is_student = True

if age >= 18 and is_student: 
    print("Estudante maior de 18")
elif age < 18:
    print("Menor de 18")
elif is_student == False:
    print("Não estudante")
