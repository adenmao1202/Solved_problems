# Figure 9.6
def getBinaryRep(n, numDigits):
    """Assumes n and numDigits are non-negative ints
    Returns a str of length numDigits that is a binary
    representation of n"""
    
    result = ""
    while n > 0: # 慣用 int to str 寫法
        result = str(n % 2) + result
        n = n // 2
    if len(result) > numDigits:
        raise ValueError("not enough digits")
    for i in range(numDigits - len(result)):
        result = "0" + result
    return result


def genPowerset(L):
    """Assumes L is a list
    Returns a list of lists that contains all possible
    combinations of the elements of L. E.g., if
    L is [1, 2] it will return a list with elements
    [], [1], [2], and [1,2]."""
    powerset = []
    for i in range(0, 2 ** len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == "1":
                subset.append(L[j])
        powerset.append(subset)
    return powerset


if __name__ == "__main__":
    L = ["x", "y"]
    print(genPowerset(L))

    L = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(genPowerset(L))
