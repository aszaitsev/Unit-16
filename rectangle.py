# Task_16.8.1
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self,a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2
# возведениеи в степень **2 (в квадрат)

# Task_16.8.2
class Circle:
    def __init__(self, r, Pi=3.14):
        self.Pi = Pi
        self.r = r
    def get_area_circle(self):
        return self.Pi * self.r ** 2