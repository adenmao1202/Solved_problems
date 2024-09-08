"""
Description
Implement a function that performs a binary search 
on a sorted array of integers to find a specific target value. The function should return the index of the target if it is present in the array, or -1 if it is not found.

Please note that the array is in a descending order.
------
Input
The input will contains multiple lines.

Odd lines will contain input array and even lines will contain target number.

0 indicates that the test was over.
-------
Output
Print out the index of founded value or -1 if not founded.

---
Input
9 8 7 5 1
7
9 8 6 5 3 2
4
0
Output
2
-1
""" 
def binary_search(lis, target):
    
    left, right = 0, len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if mid == target: 
        return mid 
    else: 
        return -1
    

def main():
    while True:
        lis = list(map(int, input().split()))
        if lis == [0]: 
            break 
        lis = lis[::-1]
        target = int(input())
        print(binary_search(lis, target)) 
               
        
if __name__ == "__main__":
    main()

