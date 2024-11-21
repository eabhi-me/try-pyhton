# Base class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Derived class
class WorkingDog(Dog):
    def __init__(self, name, age, job):
        # Call the initializer of the base class
        super().__init__(name, age)
        self.job = job

    def description(self):
        # Overriding the method from the base class
        base_description = super().description()
        return f"{base_description} and works as a {self.job}"

    def perform_job(self):
        return f"{self.name} is performing its job as a {self.job}."

# Create an instance of the derived class
working_dog = WorkingDog("Rex", 4, "search and rescue")

# Access methods from the base class
print(working_dog.description())  # Output: Rex is 4 years old and works as a search and rescue
print(working_dog.speak("Woof"))  # Output: Rex says Woof

# Access method from the derived class
print(working_dog.perform_job())  # Output: Rex is performing its job as a search and rescue.
