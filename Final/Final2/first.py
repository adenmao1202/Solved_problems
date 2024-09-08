"""
For a positive integer n, let f(n) denote the sum of the digits of n when represented in base 10.
It is easy to see that the sequence of numbersn, f(n), f(f(n)), f(f(f(n))), . . . eventually becomes a single digit number that repeats forever. Let this single digit be denoted g(n). For example, consider n = 1234567892. Then:
f(n) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 2 = 47
f(f(n)) = 4 + 7 = 11
f(f(f(n))) = 1 + 1 = 2
Therefore, g(1234567892) = 2.
"""
def digit_sum(n: int) :
    str_n = str(n)
    len_n = len(str_n)
    sum_n = 0
    while len_n > 1:
        for i in range(len_n):
            sum_n += int(str_n[i])
        str_n = str(sum_n)
        len_n = len(str_n)
        sum_n = 0
    return int(str_n)

def main():
    while True: 
        n = int(input())
        if n != 0:
            print(digit_sum(n))
        else:
            break
        
if __name__ == "__main__":
    main()
    
        