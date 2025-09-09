class Circle:
    def __init__(self,radius):
        self.radius =radius
        print("circle created")
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getPerimeter(self):
        return 2*3.14*self.radius
    
mycircle=Circle(10)
print(mycircle.getArea())
print(mycircle.getPerimeter())