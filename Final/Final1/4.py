def multiple_of_11(n): # 奇 - 偶 是0 or 11的倍數
    even_sum = 0
    odd_sum = 0
    str_n = str(n)   # str可以用index來找位數
    length_n = len(str_n)
    
    for i in range(length_n): # 遍歷所有位數
        if i % 2 == 0:  # 偶數位 : i % 2 == 0
            even_sum += int(str_n[i])
        else:  # 奇數位
            odd_sum += int(str_n[i])
    
    difference = abs(odd_sum - even_sum)  # 絕對值：abs(n)
    
    if difference == 0 or difference % 11 == 0:
        return f"{n} is a multiple of 11."
    else:
        return f"{n} is not a multiple of 11."




         
def main():
    while True: 
        num = input()
        if int(num) != 0:
            print(multiple_of_11(num))
        else:          
            break

if __name__ == "__main__":
    main()



