from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    # TODO - you fill in here.
    root = 1
    while root * root < n:
        root += 1
    primes = [True for i in range(n+1)]
    primes[0] = primes[1] = False
    for i in range(2, root+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    res = list()
    for i in range(n+1):
        if primes[i]:
            res.append(i)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
