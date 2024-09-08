# Collatz conjecture
"""
if odd: n --> 3*n + 1
if even: n --> n/2
when n = 1, stop
print(i, j, maxIterlength(i, j))
"""
def coll(n):
    length = 1
    while n != 1:
        if n % 2 == 0: 
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def maxIter(i, j):
    iteration = []
    for n in range(i, j + 1):
        iteration.append(coll(n))
    return max(iteration)

def main():
    while True:
        try:
            input_line = input().split(" ")
            i = int(input_line[0])
            j = int(input_line[1])
            if i == 0 or j == 0:
                return ""
            else:
                print(i, j, maxIter(i, j))
                
        except EOFError:
            break
    
    
if __name__ == "__main__":
    main()
   
   
