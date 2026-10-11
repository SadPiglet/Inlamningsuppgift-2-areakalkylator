from abc import ABC, abstractmethod
import math

class Shape(ABC):

  @abstractmethod
  def area(self):
    pass

class Rectangle(Shape): # Rectangle ärver från Shape

  def __init__(self, width, height): # Sparar rektangelns bredd och höjd som attribut
    self.width = width
    self.height = height

  def area(self): # Implementerar area-metoden för rektangeln och returnerar arean
    return self.width * self.height

class Square(Shape): # Square ärver från Shape

  def __init__(self, side_length):
    self.side_length = side_length

  def area(self): # Implementerar area-metoden för kvadraten och returnerar arean
    return self.side_length ** 2 # För kvadraten är arean lika med sidan upphöjt till 2

class Circle(Shape): # Circle ärver från Shape

  def __init__(self, radius):
    self.radius = radius

  def area(self): # Implementerar area-metoden för cirkeln och returnerar arean
    return math.pi * self.radius ** 2 # För cirkeln är arean lika med pi gånger radien upphöjt till 2

class Triangle(Shape): # Triangle ärver från Shape

  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self): # Implementerar area-metoden för triangeln och returnerar arean
    return 0.5 * self.base * self.height # För triangeln är arean lika med basen gånger höjden delat med 2

class Hexagon(Shape): # Hexagon ärver från Shape

  def __init__(self, side_length):
    self.side_length = side_length

  def area(self): # Implementerar area-metoden för hexagonen och returnerar arean
    return (3 * math.sqrt(3) / 2) * self.side_length ** 2 # För hexagonen är arean lika med (3 * sqrt(3) / 2) gånger sidan upphöjt till 2
