# # Find the cube root of a perfect cube

# x = int(input("Enter an integer: "))  # the input is the target number
# ans = 0  # set a variable
# while ans**3 < abs(x):  # abs = absolute value
#     ans = ans + 1
#     # loop until condition met
# if ans**3 != abs(x):
#     print(x, "is not a perfect cube")
# else:
#     if x < 0:  # to determine whethter it is negative
#         ans = -ans
# print("Cube root of", x, "is", ans)  # if not neg, directly print ' ans '

# oop 
class any_root:
    def __init__(self, target, rootdeg):
        self.target = target
        self.rootdeg = rootdeg
        
    def cal(self):
        ans = 0
        while ans ** self.rootdeg < abs(self.target):
            ans += 1
            
        if ans ** self.rootdeg != abs(self.target):
            return f"{self.target}, cannot find the {self.rootdeg } th root"
        else:
            if self.target < 0:
                ans = -ans
            return f" the {self.rootdeg}th root of {self.target} is {ans}"
            
    def __str__(self):
        return f"the {self.rootdeg}th root of {self.target} is {self.cal()}"
    
    def __repr__(self):
        return f"the {self.rootdeg}th root of {self.target} is {self.cal()}"

def main():
    target = int(input("Enter an integer: "))
    rootdeg = int(input("Enter the root degree: "))
    if rootdeg == 0 and target!= 1:
        print("The 0th root of a non-one is undefined")
    else:
        a = any_root(target, rootdeg)
        result = a.cal()
        print(result)

if __name__ == "__main__":
    main()
            