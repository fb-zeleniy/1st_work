import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle(radius={self.radius})"
    
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return False
    
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return False

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return False
    
   
    def __add__(self, value):

        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        
        elif isinstance(value, Circle):
            return Circle(self.radius + value.radius)
        return self
    
    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        
        elif isinstance(value, Circle):
            return Circle(self.radius - value.radius)
        return self
    
    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value

        elif isinstance(value, Circle):
            self.radius += value.radius
        return self
    
    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value

        elif isinstance(value, Circle):
            self.radius -= value.radius
        return self
    
    
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return self
    
    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        return self
    
    def __mul__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius * value)
        return self
    
    def __truediv__(self, value):
        if isinstance(value, (int, float)) and value != 0:
            return Circle(self.radius / value)
        raise ValueError("Деление на ноль невозможно")
    
    
    def circumference(self):
        return 2 * math.pi * self.radius


