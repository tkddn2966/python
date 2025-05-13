
class point:
    def __init__(self, x=0,y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f"{self.__x}, {self.__y}")
    
    def set(self,x,y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)



class Rectangle:
    def __init__(self, x1=0,y1=0,x2=0,y2=0):
        self.__lt = point(x1,y1)
        self.__rb = point(x2,y2)
        
        

    def show(self):
        print(f"좌측상단 꼭지점이 {self.__lt.get()}이고 우측 하단 꼭지점이 {self.__rb.get()}인 사각형입니다.")
        
    def getWidth(self):
        return self.__rb.get()[0] - self.__lt.get()[0]
    
    def getHeight(self):
        return self.__rb.get()[1] - self.__lt.get()[1]
    
    def getArea(self):
        return (self.__rb.get()[0] - self.__lt.get()[0]) * (self.__rb.get()[1] - self.__lt.get()[1])
    
    def getPerimeter(self):
        return (self.__rb.get()[0] - self.__lt.get()[0]) + (self.__rb.get()[1] - self.__lt.get()[1])*2
    



r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"넓이는 {a}, 둘레는 {p}")

