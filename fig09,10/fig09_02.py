#Figure 9.2
def squareRootBi(x, epsilon):
   low = 0.0
   high = max(1.0, x)
   ans = (high + low)/2.0
   while abs(ans**2 - x) >= epsilon:
      if ans**2 < x:
         low = ans
      else:
         high = ans
      ans = (high + low)/2.0
   return ans

if __name__ == '__main__':
    print(squareRootBi(100, 0.0001))

