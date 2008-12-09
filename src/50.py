from util import sieve

def solve():
    last = 1000000
    result = 0
    max_len = 0
    primes = sieve(last)
    prime_set = set(primes)
    for i in xrange(len(primes)):
        for j in xrange(i + max_len + 1, len(primes) + 1):
            prime = sum(primes[i:j])
            if prime >= last:
                break
            if prime in prime_set:
                max_len = j - i
                result = prime
    return result

if __name__ == '__main__':
    print solve()
