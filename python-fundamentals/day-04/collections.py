# List

students = ["Eduardo", "Lucas", "Marcos", "Ana"]

print(students)
print(students[0])
print(students[1])

# Adicionar Elemento
students.append("Pedro")

# Remover Elemento
students.remove("Lucas")

# Quantidade de Elementos
print(len(students))

# Percorrer lista
for student in students:
    print(student)

# Exemplo 1
languages = ["Java", "Python", "JavaScript"]

languages.remove("JavaScript")

languages.append("SQL")

print(len(languages))

for language in languages:
    print(language)
    
# Tuple

students = ("Eduardo", "Lucas", "Marcos", "Ana")

print(students)
print(students[0])
print(students[1])

# Exemplo 2
student = ("Eduardo", 19, "Engenharia de Software", 4)

print(student)
print(student[0])
print(student[-1])

print(len(student))

for info in student:
    print(info)
    
# Set

languages = {"Java", "Python", "JavaScript", "Python"}

print(languages)

languages.add("SQL")
languages.remove("Java")

print(languages)

for language in languages:
    print(language)
    
# Exemplo 3
languages = {"Java", "Python", "JavaScript", "Python"}

languages.add("SQL")
languages.remove("JavaScript")

print(len(languages))

for language in languages:
    print(language)
    
# Dictionary

student = {
    "name": "Eduardo",
    "age": 19,
    "course": "Engenharia de Software",
    "semester": 4,
}

print(student)
print(student["name"])
print(student["age"])

# Adicionar informação
student["university"] = "Universidade Católica do Salvador"

# Modificar informação
student["semester"] = 5

# Remover informação
student.pop("name")
print(student)

for key, value in student.items():
    print(f"{key}: {value}")
    
# Exemplo 4

student = {
    "name": "Clarencio",
    "age": 10,
    "course": "Medicine",
    "semester": 6,
}

print(student["course"])

student["university"] = "MIT"
student["semester"] = 7

student.pop("age")

for key, value in student.items():
    print(f"{key}: {value}")