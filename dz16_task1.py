class Device:
    
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year  

    def __str__(self):
        return f"{self.__class__.__name__} {self.brand} {self.model}, год выпуска: {self.year}Вт"


class CoffeeMachine(Device):
   
    def __init__(self, brand, model, year, wate_capacity):
        super().__init__(brand, model, year)
        self.water_tank_capacity = wate_capacity  
    
class Blender(Device):
    
    def __init__(self, brand, model, year, speed_levels):
        super().__init__(brand, model, year)
        self.speed_levels = speed_levels  
    
class MeatGrinder(Device):
   
    def __init__(self, brand, model, year, meat):
        super().__init__(brand, model, year)
        self.meat = meat  

    