def findExtremeDivisors(n1, n2):
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):  # i 最大只會到 min(n1, n2)
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)


if __name__ == "__main__":
    minDivisor, maxDivisor = findExtremeDivisors(10, 20)
    print(minDivisor, maxDivisor)
