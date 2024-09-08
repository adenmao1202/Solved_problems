# roman to integer 

"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
---------------------------------------
Input
Input is a Roman numeral in string.

We note that

1 <= s.length <= 15
Input may be more than one roman numerals.
---------------------------------------
Output
Output is an integer.

The value converted by s will be in the range of 
[1,3999]
"""

def romanToInt(s): # 排序照理說都會是大到小，如果不是，就是減法
    """
    :type s: str
    :rtype: int
---------------
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
    """
    # 舉例： CXIV = 1404
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    tot = 0 
    for i in range(len(s) - 1): # 只取到倒數第二位，因為最後一位沒有辦法跟下一位比較       
        if roman[s[i]] < roman[s[i + 1]]:
            tot -= roman[s[i]]  # 由於是大到小，所以如果小到大，那一定是剪法
            
        else:
            tot += roman[s[i]]
    result = tot + roman[s[-1]]
    return result 

def main():
    while True: 
        try:
            s = input() # str 
            print(romanToInt(s))
            
        except EOFError:
            break



if __name__ == '__main__':
    main()