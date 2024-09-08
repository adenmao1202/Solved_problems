def var(x):
    times = 1
    while x != 1:
        if x % 3 == 0:
            x = x // 3 
        elif x % 3 == 1: 
            x = 4 * x + 1
        else:
            x = 2 * x + 2 
        times += 1
    return times

def maxIter(i, j):
    max_iter = 0
    for n in range( i , j + 1):
        current = var(n)
        if current > max_iter:
            max_iter = current
    return max_iter

# def main():
#     while True:
#         try: 
#             line = input()
#             print(line)
#             if not line:
#                 raise EOFError
            
#             line = line.split(" ")
#             print(line)
#             if len(line) != 2:
#                 raise ValueError
            
#             if not line[0].isdigit() or not line[1].isdigit():
#                 raise TypeError
            
#             n1 = int(line[0])
#             n2 = int(line[1])
#             print(n1, n2)    
#             if n1 > n2 or n1 <= 0 or n2 <= 0:
#                 raise ValueError
            
#             result = maxIter(n1, n2)
#             print(n1, n2, result)
    
#         except ValueError:
#             print("Invalid value")
            
#         except TypeError:
#             print("Invalid type")
            
#         except EOFError:
#             break

if __name__ == "__main__":
    print(maxIter(1, 10))
    print(var(10))