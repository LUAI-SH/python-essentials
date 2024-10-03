'''
Glossary
https://docs.python.org/3/glossary.html
'''


# Declaration
class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('drawing...')


point = Point(1, 2)
point.draw()
print(isinstance(point, Point))  # True


# Class vs Instance method, attribute
class Rectangle:
    default_color = 'green'  # class attribute

    def __init__(self, length, height):
        self.length = length  # instance attribute
        self.height = height

    @classmethod # class method
    def change_default_color(cls, color):
        cls.default_color = color

    def draw(self):
        print('drawing...')


Rectangle.change_default_color('yellow')
print(Rectangle.default_color)


# Private Members
class Echo:
    __log_counter = 10 # private 
    

# Properties
class Product:
    def __init__(self, price):
        self.price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        # validate...
        self.__price = price
        
        
# Inheritance
class Shape:
    def __init__(self, color):
        self.color = color
        
class Triangle(Shape):
    def __init__(self, color):
        super().color = color
        
# Abstract class
from abc import ABC, abstractmethod
class Stream(ABC):
    @abstractmethod 
    def read(self):
        pass
    
class FileStream(Stream):
    def read(self):
        print('reading from file...')
    
file_stream = FileStream()
file_stream.read()