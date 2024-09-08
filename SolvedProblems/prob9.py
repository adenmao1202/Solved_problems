"""
Description:

As what you learned in the past few weeks, now let's do some practice of function overloading. You are asked to design a class "Vector", which includes the following methods:

constructor ( Vector(x,y,z) )

overload operator +

overload operator -

overload operator ==

overload operator * as dot operation

overload operator ^ as cross operation

overload str() method

Input Format:

You don't need to handle input strings.The first line contains one positive integer N, 
means there will be N vectors given.
The next N lines will each be a vector, in the format of "x y z".
Rest of the lines are operations, in the format of "(vector number) (vector number) (operator)".

Output Format:

You don't need to write output method.The string format of a vector should be defiened as follow:str(Vector) = [x, y, z]
"""
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = [x, y, z]
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __xor__(self, other):
        cross_x = self.y * other.z - self.z * other.y
        cross_y = self.z * other.x - self.x * other.z
        cross_z = self.x * other.y - self.y * other.x
        return Vector(cross_x, cross_y, cross_z)
    
    def __str__(self):  # Corrected string format
        return f"[{self.x}, {self.y}, {self.z}]"
    
    def __repr__(self):  # Corrected string format
        return f"[{self.x}, {self.y}, {self.z}]"


def calc(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "eq":
        return a == b
    elif op == "dot":
        return a * b
    elif op == "cross":
        return a ^ b
        


if __name__ == "__main__":
    n = int(input())
    list = []
    for i in range(n):
        x, y, z = input().split(" ")
        list.append(Vector(int(x), int(y), int(z)))
        
    print(list)
    
    while True:
        try:
            command = input().split(" ")
            if len(command) != 3:
                continue
            a = list[int(command[0]) - 1]
            b = list[int(command[1]) - 1]
            print(calc(a, b, command[2]))
            
        except IndexError:
            raise IndexError("Index out of range")
        except EOFError:
            exit()