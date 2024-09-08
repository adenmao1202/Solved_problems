# Ch9.3


def intToStr(i):
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result


def addDigits(n):
    stringRep = intToStr(n)
    val = 0
    for c in stringRep:
        val += int(c)
    return val


if __name__ == "__main__":
    print(intToStr(10))
    print(addDigits(102))
