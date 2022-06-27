def prime_list(x):
    n = 2
    primes = []
    while True and len(primes) < x:
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n
        n += 1


N = int(input())
y = prime_list(N)
print(*y)



#  def prime_generator():
#    n = 1
#    while True:
#        n += 1
#        if is_prime(n):
#            yield n
