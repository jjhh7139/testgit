PI = 3.141592 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calcPerimeter(self):
        self.calcperimeter = PI * 2 * self.radius
    def calcArea(self):
        self.calcarea = PI * (self.radius**2)
    def __str__(self):
        msg = "반지름: "+str(self.radius) +" 원의 면적: "+str(self.calcarea) +" 원의 둘레: "+str(self.calcperimeter)
        return msg

myCircle = Circle(100)
myCircle.calcPerimeter()
myCircle.calcArea()
print(myCircle)
