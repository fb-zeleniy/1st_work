class Book:
     def __init__(self, book_name,year, publisher, zhanr, author, price):

        self.book_name = book_name
        self.year = year
        self.publisher = publisher
        self.zhanr = zhanr
        self.author = author
        self.price = price 

        
     def specifications(self):
        print(f"Book name: {self.book_name}")
        print(f"Year: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Zhanr: {self.zhanr}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")



     def set_book_name(self, book_name):
        self.book_name = book_name

     def set_year(self, year):
        self.year = year

     def set_publisher(self, publisher):
        self.publisher = publisher

     def set_zhanr(self, zhanr):
        self.zhanr = zhanr

     def set_author(self, author):
        self.author = author

     def set_price(self, price):
        self.price = price

     def get_book_name(self):
        return self.book_name

     def get_year(self):
        return self.year

     def get_publisher(self):
        return self.publisher

     def get_zhanr(self):
        return self.zhanr

     def get_author(self):
        return self.author

     def get_price(self):
        return self.price

 
  
     