import pickle
class Shape:
    def __init__(self, name):
        self.name = name
    
    def Show(self):
        raise NotImplementedError("Метод 'Show' должен быть реализован в производном классе")
    
    def Save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    
    
    def Load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

class Square(Shape):
    def __init__(self, x, y, length):
        super().__init__("Square")
        self.x = x  
        self.y = y
        self.length = length

    def Show(self):
        print(f"Фигура: {self.name}")
        print(f"Коор-ты левого верхнего угла: ({self.x}, {self.y})")
        print(f"Длина стороны: {self.length}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__("Rectangle")
        self.x = x  
        self.y = y
        self.width = width  
        self.height = height  

    def Show(self):
        print(f"Фигура: {self.name}")
        print(f"Коор-ты левого верхнего угла: ({self.x}, {self.y})")
        print(f"Длина стороны: {self.height}")