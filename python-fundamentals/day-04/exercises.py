# Exercício 1 - List
students = ["Clarencio", "Robin", "Jake"]
students.append("Art")
print(len(students))

# Exercício 2 - Tuple
courses = ("Medicine", "Software engineer", "Physiotherapy")
print(courses[1])

# Exercício 3 - Set
skills = {"Java", "Python", "SQL", "Python"}
skills.add("Git")
print(len(skills))

#Exercício 4 - Dictionary
student = {
    "name": "Robin",
    "age": 18,
    "course": "Software engineer"
}

student["university"] = "MIT"

for key, value in student.items():
    print(f"{key}: {value}")

