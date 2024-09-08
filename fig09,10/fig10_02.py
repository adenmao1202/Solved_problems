# Figure 10.2
def search(L, e):
    """Assumes L is a list, the elements of which are in
       ascending order --> 已經排序的list
    Returns True: if e is in L
    and False otherwise
    """
    for i in range(len(L)):  # 假設排序好的狀況
        if L[i] == e:
            return True
        if L[i] > e: # 因為假設排序，所以如果大於的話，就證明這個要找的元素不在list中
            return False
    return False # 如果沒大於的狀況，也沒找到





if __name__ == "__main__":
    L1 = [1, 3, 2, 4]
    L2 = sorted(L1)  # 排序
    print(L2)
    print(search(L2, 5))
