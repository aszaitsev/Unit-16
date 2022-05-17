# Task_16.9.1
class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

# Task_16.9.2
    def get_area(self):
        return self.width * self.heigth

    def __str__(self):
        return f'{self.x}, {self.y}, {self.width}, {self.heigth}'


rect_1 = Rectangle(5, 10, 50, 100)

print(f'Rectangle: {rect_1.__str__()}.')
print(f'Area: {rect_1.get_area()}.')


