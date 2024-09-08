# Figure 10.4
def selSort(L):  # selection sort
    """Assumes that L is a list of elements that can be
      compared using >.
    Sorts L in ascending order"""
    
    suffixStart = 0
    while suffixStart != len(L):
        # look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                # swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
            
        suffixStart += 1


if __name__ == "__main__":
    L = [10, 7, 9]
    
    # [7, 10, 9]
    # [7, 9, 10]
    selSort(L)
    print(L)
