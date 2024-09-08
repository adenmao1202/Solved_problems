# prime number 
def find_prime(n: str):
    if int(n) <= 1:
        return f"{int(n)} is not a prime number"
    for i in range (2, int(int(n)** 0.5) + 1):
        if int(n) % i == 0:
            return f"{int(n)} is not a prime number"
    else:
        return f"{int(n)} is a prime number" # 以上兩個都通過，如果都沒有return, 則為prime number
        
def main():
    while True:
        num = input()
        if int(num) == 0:
            break
        else:
            print(find_prime(num))
            
if __name__ == "__main__":
    main()
