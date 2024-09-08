""" 
Description
Given a range [a, b], you are to find the summation of all the odd integers 
in this range. For example,
the summation of all the odd integers in the range [3, 9] is 3 + 5 + 7 + 9 = 24.
Input
---
Input
There can be at multiple test cases. 
The first line of input gives you the number of test cases, T (1 ≤ T ≤ 100). 
Then T test cases follow. Each test case consists of 2 integers a and b (0 ≤ a ≤ b ≤ 1000)
in two separate lines.
---
Output
For each test case you need to print the summation of the odd integers in the range [a, b].
"""
def odd_sum(a, b):
    odd_sum = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            odd_sum += i
    return odd_sum

def main():
    test_case = int(input())
    for i in range(test_case):
        a = int(input())
        b = int(input())
        print(odd_sum(a, b))
        
if __name__ == "__main__":
    main()