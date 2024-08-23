import math


class Vector2:
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

    def normalize(self):
        len = math.sqrt(self.x*self.x+self.y*self.y)
        if len == 0:
            return self
        return self/len
    
    @staticmethod
    def right():
        return Vector2(1,0)
    
    @staticmethod
    def left():
        return Vector2(-1,0)
    
    @staticmethod
    def up():
        return Vector2(0,-1)
    
    @staticmethod
    def down():
        return Vector2(0,1)
    
    @staticmethod
    def one():
        return Vector2(1,1)
    
    @staticmethod
    def zero():
        return Vector2(0,0)

    @staticmethod
    def distance(a,b):
        dir = b - a
        len = math.sqrt(dir.x*dir.x+dir.y*dir.y)
        return len

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        return NotImplemented