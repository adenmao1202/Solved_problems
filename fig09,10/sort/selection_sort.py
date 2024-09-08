"""
https://en.wikipedia.org/wiki/Selection_sort

This is a pure Python implementation of the selection sort algorithm

For doctests run following command:
python -m doctest -v selection_sort.py
or
python3 -m doctest -v selection_sort.py

For manual testing run:
python selection_sort.py
"""


def selection_sort(L):
    """Pure implementation of the selection sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending


    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(L)
    for i in range(length - 1): # 先選定第一個
        least = i
        for k in range(i + 1, length):
            if L[k] < L[least]: # 如果除了第一個之外，有更小的，就選定起來（變紅色）
                least = k          
        
        if least != i: # 交換元素：這時候Least 被改為K了，如果兩者不相等，就交換
            # L[least], L[i] = (L[i], L[least])
            L[i], L[least] = L[least], L[i]
    return L


   
            

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(unsorted)
    print(selection_sort(unsorted))
