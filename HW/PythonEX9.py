class Complex:
    def __init__(self, real, imag):
        self.real = int(real)  # real part
        self.imag = int(imag)  # imagined part

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def __floordiv__(self, other):
        return Complex(
            (self.real * other.real + self.imag * other.imag)
            // (other.real**2 + other.imag**2),
            (self.imag * other.real - self.real * other.imag)
            // (other.real**2 + other.imag**2),
        )

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __str__(self):
        if self.imag == 0:
            return str(self.real)
        elif self.real == 0:
            return str(self.imag) + "i"
        elif self.imag < 0:
            return str(self.real) + str(self.imag) + "i"
        else:
            return str(self.real) + "+" + str(self.imag) + "i"

def cmd(command, a, b):
    if command == "add":
        print(a + b)
    elif command == "sub":
        print(a - b)
    elif command == "mul":
        print(a * b)
    elif command == "floordiv":
        print(a // b)
    elif command == "conjugate":
        print(a.conjugate())
        print(b.conjugate())
    elif command == "end":
        return False  # 只有到這邊，while True才會跳出, 
    return True # 其他情況，都會不斷執行下去

# 以下不用上傳
if __name__ == "__main__":
    # 傳入兩個複數
    tmp = input().split(" ")
    a = Complex(int(tmp[0]), int(tmp[1]))
    tmp = input().split(" ")
    b = Complex(int(tmp[0]), int(tmp[1]))
    
    # 操作
    
    while True:
        command = input()
        if not cmd(command, a, b):
            break

