# Ch9.1


def f(i):
    """Assumes i is an int and i >= 0"""
    answer = 1
    while i >= 1:
        answer *= i   # answer = answer * i
        i -= 1 # i = i - 1
    return answer # 最後才打印出來 （ when i = 1 ) 


def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False


def fact(n):
    """Assumes n is a natural number Returns n!"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer


if __name__ == "__main__":
    print(f(5))

    L = [1, 2, 3]
    print(linearSearch(L, 2))

    print(fact(10))
