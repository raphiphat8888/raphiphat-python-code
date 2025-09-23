"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle :
    def __init__(self,leght,width):
        self.__leght=leght
        self.__width=width
        
    def GetArea(self):
        area=self.__leght * self.__width
        return f" area = {area}"
    
    def getPerimeter(self):
         print(f"perimeter={self.__leght + self.__width*2}")

    def isSquare(self):
        if self.__leght==self.__width:
            return True
        else:
            return False
myRectangle=Rectangle(10,2)

print(myRectangle.GetArea())
myRectangle.getPerimeter()
print(myRectangle.isSquare())



