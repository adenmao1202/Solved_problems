# # Binary search 
# def Bin_search(L, target):
#     for i in range(len(L)):
#         if int(L[i]) == target:
#             return i

#     return -1 

# def main():
#     L = input().split() 
#     target = int(input())
#     print(Bin_search(L, target))
        
# if __name__ == "__main__":
#     main()

def bi_search (lis, target):
    left = 0
    right = len(lis) - 1  # 因為index從 0 開始

    while left <= right:
        mid = left + (right - left) // 2  # finding target
        current_item = lis[mid]
        if current_item == target:
            return mid
        elif target < current_item:
            right = mid - 1
        else:
            left = mid + 1
    if mid == target:
        return mid
    
    if mid != target:
        return -1

def main():
    try: 
        lis = list(map(int, input().split()))
        target = int(input())
        print(bi_search(lis, target))
        
    except ValueError:
        print("Invalid value")
        
if __name__ == "__main__":
    main()