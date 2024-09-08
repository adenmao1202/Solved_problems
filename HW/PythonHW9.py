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

    def __eq__(self, other):  # limited usage of ==
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __xor__(self, other):
        cross_x = self.y * other.z - self.z * other.y
        cross_y = self.z * other.x - self.x * other.z
        cross_z = self.x * other.y - self.y * other.x
        return Vector(cross_x, cross_y, cross_z)  # 放回vector的format

    def __str__(self):  # Corrected string format
        return f"[{self.x}, {self.y}, {self.z}]"


def calc(a, b, command):
    if command == "add":
        return a + b
    elif command == "sub":
        return a - b
    elif command == "dot":
        return a * b
    elif command == "cross":
        return a ^ b
    elif command == "equal":
        return a == b


# main func for testing purposes (not for submission)
if __name__ == "__main__":
    n = int(input())
    list = []
    for i in range(n):
        x, y, z = input().split(" ")
        list.append(Vector(int(x), int(y), int(z)))
    while True:
        try:
            command = input().split(" ")
            if len(command) != 3:
                continue
            if int(command[0]) <= n and int(command[1]) <= n:
                a = list[int(command[0]) - 1]
                b = list[int(command[1]) - 1]
                print(calc(a, b, command[2]))
                
            else:
                raise IndexError("Index out of range")
        except EOFError:
            exit()
