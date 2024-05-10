# Figure 6.3
def isPal(x):
    temp = x[:]  # Make a copy of the list
    temp.reverse()  # Correctly reverse the list
    if temp == x:
        return True
    else:
        return False


def silly(n):
    """Assumes n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the sequence of inputs forms a palindrome;
        'No' otherwise"""
    result = []  # ---> empty list usually are outside of for loop
    for i in range(n):
        elem = input("Enter element: ")
        result.append(elem)

    if isPal(result):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    silly(5)
