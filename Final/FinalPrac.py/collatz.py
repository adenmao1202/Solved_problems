"""
sum_digits_cycle(9875) -> 2
# Explanation: 9 + 8 + 7 + 5 = 29, 2 + 9 = 11, 1 + 1 = 2

max_cycle_iterations(10, 15) -> 2
"""

# def sum_digits_cycle(n: str):
#     tot = 0
#     length = 0
#     while len(n) > 1:
#         for i in range(len(n)): # 9875
#             toList = list(n)
#             print(toList)
#             tot += int(toList[i]) # sum = 29 
#         n = tot # n = 29
#         length += 1
#         tot = 0
#     return length 

def sum_digits_cycle(n):
    # process val
    def sum_digits(n: int):
        return sum(int(digit) for digit in str(n))
    
    
    # count iterations
    iterations = 0
    while int(n) >= 10:    #只有大於10的數才會iterate 
        n = sum_digits(n)  # n: int
        iterations += 1
    return iterations      # 如果while結束就會跳出來，個位數就return 

def max_cycle_iterations(n1: int, n2: int):
    max_cycle = 0
    for i in range (n1, n2 + 1): 
        if sum_digits_cycle(i) > max_cycle:
            max_cycle = sum_digits_cycle(i)
    return max_cycle
    
if __name__ == "__main__":
    line = input().split(" ")
    n1 = int(line[0])
    n2 = int(line[1])
    print(max_cycle_iterations(n1, n2))


