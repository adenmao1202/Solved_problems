def find_primes(n):
    primes = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


n1 = int(input())
n2 = int(input())
print(max(find_primes(max(n1, n2))))
