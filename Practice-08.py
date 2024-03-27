def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

primes_generator = next_prime()

# Print first 10 prime numbers for demonstration
for _ in range(10):
    print(next(primes_generator))

