# Figure 9.4


def isSubset(L1, L2): # L1 is subset of L2 or not
    """Assumes L1 and L2 are lists.
    Returns True if each element in L1 is also in L2
    and False otherwise."""
    for e1 in L1:
        matched = False # 先預設為FALSE
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


if __name__ == "__main__":
    L1 = [1, 2, 5]
    L2 = [2, 1, 3, 4]
    print(isSubset(L1, L2))
