""" 
1. 兩個input: int 
2. 找出 range(2, max(input1, input2)）的最大質數
3. 找質數 
    把小於自己的數都除一遍，如果餘數都!= 0, 就是質數
"""


def find_max_prime(num1, num2):
    big = max(num1, num2)

    all_primes = []
    for i in range(2, big):  # big = 5 , produce: 2, 3, 4
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            all_primes.append(i)
    return max(all_primes)


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print(find_max_prime(num1, num2))
