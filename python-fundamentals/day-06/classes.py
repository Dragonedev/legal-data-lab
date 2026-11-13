class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        
student1 = Student("Eduardo", 18)

student1.introduce()

# Exercício 1
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def show_info(self):
        print(f"Produto: {self.name} | Price: {self.price} | Quantity: {self.quantity}")
        
    # Exercício 2
    def add_stock(self, amount):
        self.quantity += amount
        
    # Exercício 3
    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Estoque insuficiente")
        
product1 = Product("Notebook", 3500, 10)
product2 = Product("Mouse", 80, 25)

product1.show_info()
product2.show_info()
product1.add_stock(5)
product1.show_info()
product1.remove_stock(1)
product1.show_info()

# Exercício 4 - Encapsulamento
class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        
# Exercício 5 
class Product:
    def __init__(self, quantity):
        self._quantity = quantity
        
    @property
    def quantity(self):
        return self._quantity
    
    # Exercício 6
    @quantity.setter
    def quantity(self, quantity):
            if quantity >= 0:
                self._quantity = quantity
            else:
                print("Quantidade Inválida!")

product = Product(10)
print(product.quantity)
product.quantity = 13
print(product.quantity)
product.quantity = -5
print(product.quantity)

# Try, Except e Finally
try:
    number = int(input("Digite um número: "))
    print(number)
    
except ValueError:
    print("Você precisa digitar um número inteiro!")
    
finally:
    print("Programa finalizado")
    
# Exercício 8

try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    
    total = n1/n2
    print(total)

except ValueError:
    print("Valor inválido")
    
except ZeroDivisionError:
    print("Divisão inválida")
    
finally:
    print("Operação encerrada")



    