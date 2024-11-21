class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')

class Square(Shape):
    def __init__(self,side,name="Square"):
        super().__init__(name)
        self.side = side
    
    def compute_area(self):
        return self.side*self.side
    
    def comput_perimeter(self):
        return 4*self.side
