# class Person:
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

# # Create an instance
# person1 = Person("Alice", 30)
# print(person1.name)  # Output: Alice
# print(person1.age)   # Output: 30




# # Another class
# class Car:
#     wheels = 4  # Class attribute (shared by all instances)

#     def __init__(self, color):
#         self.color = color  # Instance attribute (unique to each instance)

#     def intoduce(self):
#         print(f'This car has {self.wheels} wheel ans its color is {self.color}')

# car1 = Car("red")
# car2 = Car("blue")

# print("\nPlaying with another class: not a part of class")
# print(car1.color)   # Output: red
# print(car2.wheels)  # Output: 4
# print(car2.color)   # Output: blue
# car2.intoduce()
# car1.intoduce()




# class MyClass:
#     class_variable = "class level"

#     @classmethod
#     def class_method(cls):
#         return f"Called class_method: {cls.class_variable}"

#     @staticmethod
#     def static_method():
#         return "Called static_method"

# # Using class and static methods
# print("\nPlaying with another class: not a part of class")
# print(MyClass.class_method())  # Output: Called class_method: class level
# print(MyClass.static_method())  # Output: Called static_method




# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def sound(self):
#         return "Some sound"

# class Dog(Animal):  # Dog is inheriting from Animal
#     def sound(self):
#         return "Woof!"

# # Using inheritance
# dog = Dog("Buddy")
# print(dog.name)      # Output: Buddy (inherited from Animal)
# print(dog.sound())   # Output: Woof! (overridden method)





# '''
# Special Methods (Magic Methods)
# Special methods, also called "magic methods" (beginning and ending with double underscores, like __init__), allow instances to behave like built-in types.

# Examples of Magic Methods
# __str__ and __repr__: Define how instances are represented as strings.
# __len__: Define behavior for len() on an instance.
# __add__: Define behavior for the + operator */

# '''
# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
    
#     def __str__(self):
#         return f"{self.title}, {self.pages} pages"
    
#     def __len__(self):
#         return self.pages

# book = Book("Python Basics", 300)
# print(book)           # Output: Python Basics, 300 pages
# print(len(book))      # Output: 300




# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# # Usage
# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())  # Output: 150





# class Employee:
#     raise_amount = 1.05  # Class attribute

#     def __init__(self, name, salary):
#         self.name = name          # Instance attribute
#         self.salary = salary       # Instance attribute

#     def apply_raise(self):
#         self.salary = int(self.salary * Employee.raise_amount)

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

#     @staticmethod
#     def is_workday(day):
#         return day.weekday() < 5

#     def __str__(self):
#         return f"Employee(name={self.name}, salary={self.salary})"

# # Usage
# employee1 = Employee("John Doe", 50000)
# employee1.apply_raise()
# print(employee1)  # Output: Employee(name=John Doe, salary=52500)

# # Class method and static method usage
# Employee.set_raise_amount(1.10)
# print(Employee.raise_amount)  # Output: 1.10

# import datetime
# my_date = datetime.date(2024, 11, 21)
# print(Employee.is_workday(my_date))  # Output: True or False depending on the day






class Question:
    def __init__(self, statement, marks):
        self.statement = statement
        self.marks = marks

    def print_question(self):
        print(self.statement)

    def update_marks(self, marks):
        self.marks = marks
    
    def getMark(self):
        return self.marks

q1 = Question("What is valeus of pi",1)
print(q1.marks)

class NAT(Question):
    def __init__(self, statement, marks, answer):
        super().__init__(statement, marks)
        self.answer = answer

    def update_answer(self, answer):
        self.answer = answer

n1 = NAT("2*8+6", 1,22)
n1.print_question()
print(n1.marks)
print(n1.getMark())
