""" 
Find the sum of encrypted integers

Description
You are given an integer array nums containing positive integers. 
We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

Input
Input will be a sequence of integer. For example: 1 2 3.

The length of sequence: 
1
<
𝑛
<
1000
1<n<1000
Input type: string
Output
Return the sum of encrypted elements.

Output type: int
""" 
def encrypt(nums:str):
    max_num = max(str(i) for i in nums)
    string = ""
    for i in range(len(nums)):
       string += max_num
    return int(string)

def main():
    lis = input().split() # list of str
    len_lis = len(lis)
    tot = 0
    for i in range(len_lis):
        tot += encrypt(lis[i])   
    print(tot)
        
if __name__ == "__main__":
    main()