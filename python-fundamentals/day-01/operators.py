number1 = 10
number2 = 3

print(number1 + number2)
print(number1 / number2)
print(number1 % number2)

age = 18

print(age >= 18)
print(age < 18)

age = 20
has_permission = True

print(age >= 18 and has_permission)

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print(n1 + n2)
print(n1 - n2)
print(n1 / n2)
print(n1 * n2)

age = int(input("Digite sua idade: "))

if age < 18:
    print("Menor de idade")
elif age == 18:
    print("Idade 18 anos")
else:
    print("Maior de 18 anos")

age = 20
is_student = True

if age >= 18 and is_student:
    print("Estudante maior de 18")

elif age < 18 or is_student:
    print("Menor de 18 ou estudante")

elif is_student == False:
    print("Não estudante")