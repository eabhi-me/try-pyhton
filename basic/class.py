class Student:
    count = 0
    def __init__(self, name, roll, maths, physics, chemistry):
        Student.count += 1
        self.roll = roll
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry 

class Group:
    def __init__(self):
        self.members = [ ]

    def add(self, student):
        self.members.append(student)

    def print_members(self):
        for student in self.members:
            print(student.name)
    def remove(self, roll):
        found = False
        for student in self.members:
            if student.roll == roll:
                found = True
                break
        if found:
            self.members.remove(student)
        else:
            print('Student not found')

       

student1 = Student("Wells",2,45,45,89)
student2 = Student("Abhi",5,78,89,98)
groupA = Group()
groupA.add(student2)
groupA.add(student1)
groupA.print_members()
print(Student.count)
groupA.remove(2)
groupA.print_members()
print(Student.count)
