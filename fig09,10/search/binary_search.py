"""
This is pure Python implementation of binary search algorithms

For doctests run following command:    # 可以拿來當測試用（用準備好的範例）
python3 -m doctest -v binary_search.py

For manual testing run:
python3 binary_search.py

https://en.wikipedia.org/wiki/Binary_search_algorithm
"""

from __future__ import annotations


def binary_search(sorted_collection: list[int], item: int) -> int | None:
    """Pure implementation of binary search algorithm in Python

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable

    # parameters explained
    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:     -------->  test case provided by designers
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search([0, 5, 7, 10, 15], 6)

    """
    left = 0
    right = len(sorted_collection) - 1  # 因為index從 0 開始

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


def binary_search_by_recursion(
    sorted_collection: list[int], item: int, left: int, right: int
) -> int | None:
    """Pure implementation of binary search algorithm in Python by recursion

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 0, 0, 4)
    0

    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 15, 0, 4)
    4

    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 5, 0, 4)
    1

    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 6, 0, 4)

    """
    if right < left:
        return None

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()

    collection = sorted(int(item) for item in user_input.split(","))

    target = int(input("Enter a single number to be found in the list:\n"))

    result = binary_search(collection, target)
    if result is None:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} in {collection}.")
