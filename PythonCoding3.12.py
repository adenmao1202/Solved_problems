# Python Coding 3.12
def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
        epsilon > 0 & power >= 1
    Returns float y such that y**power is within epsilon of x.
        If such a float does not exist, it returns None"""

    if x < 0 and power % 2 == 0:  # Negative number has no even-powered roots
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0  # first (1+ 0) / 2 = 0.5 # 但仍會回到上方 while
    return ans


# Main
def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:  # 0.25, -0.25, 2, -2, 8, -8
        for power in range(1, 4):  # 1, 2, 3
            print("Testing x =", str(x), "and power = ", power)
            result = findRoot(
                x, power, epsilon
            )  # 呼叫上方的 function, 呼叫完的return回到
            if result == None:
                print("   No root")
            else:
                print("    ", str(result), "**", str(power), "~=", x)  # ~= approximate


testFindRoot()
