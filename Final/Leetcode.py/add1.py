""" 
You are given a large integer represented as an integer array digits, 

where each digits[i] is the ith digit of the integer. 

The digits are ordered from most significant to least significant in left-to-right order. 

The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



-------------
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
""" 
from typing import List

def add1(dig: List[int]) -> List[int]:
    
    n = len(dig)
    
    # Iterate from the last digit towards the first
    for i in range(n-1, -1, -1): # 因為進位法則，從最好一位開始到第0位, 因此要到-1, 因為range不會包括最後一位
        if dig[i] < 9:           
            dig[i] += 1
            return dig
        else:
            dig[i] = 0                   # e.g.dig = [9, 9] --> dig[1] = 0, dig[0] = 0 
    
    # If all digits were 9
    return [1] + dig   

def main():
    line = list(map(int, input().split()))
    print(add1(line))

if __name__ == "__main__":
    main()
    
    

    
    