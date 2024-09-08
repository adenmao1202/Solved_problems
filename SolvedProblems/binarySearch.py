## 
# x = 25
# epsilon = 0.01
# numGuesses = 0 # 猜幾次
# # 多出來的
# low = 0.0
# high = max(1.0, x) # x 可以比1小，因為我們取max 
# ans = (high + low)/2.0

# while abs(ans **2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1 
#  # 下判斷 
#     if ans**2 < x:
#         low = ans
#     else: # ans 的平方若大於 x, 改 high , 等於
#         high = ans
#     ans = (high + low)/2.0
  
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)


# oop 
class Bin_search:
    
    def __init__(self, target, epsilon):
        self.target = target
        self.epsilon = epsilon
        
        
    def cal(self):
        
        low = 0.0
        high = max(1.0, self.target) 
        ans = (high + low)/2.0
        numGuesses = 0 # 猜幾次
        
        while abs(ans **2 - self.target) >= self.epsilon:
            print('low =', low, 'high =', high, 'ans =', ans)
            numGuesses += 1 
            if ans**2 < self.target:
                low = ans
            else: # ans 的平方若大於 x, 改 high , 等於
                high = ans
            ans = (high + low)/2.0
        
        self.numGuesses = numGuesses
        self.ans = ans
    
    def get_numGuesses(self):
        return self.numGuesses
    
    def __str__(self):
        return f" {self.ans} is the square root of {self.target} "
    
def main():
    target = int(input("Enter an integer: "))
    epsilon = float(input("Enter an epsilon: "))
    result = Bin_search(target, epsilon)
    result.cal()
    result.get_numGuesses()
    print(result, "numGuesses = ", result.get_numGuesses())
        
if __name__ == '__main__':
    main()