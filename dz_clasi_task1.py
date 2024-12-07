class Car:
    def __init__(self, model, year, brand, obiem, color, price):

        self.model = model
        self.year = year
        self.brand = brand
        self.obiem = obiem
        self.color = color
        self.price = price 

        
    def specifications(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Brand: {self.brand}")
        print(f"Obiem: {self.obiem}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
  
    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.__year = year

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_obiem(self):
        return self.obiem 

    def set_obiem(self,obiem):
        self.obiem = obiem      

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


