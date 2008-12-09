from itertools import count

def sieve(last):
    primes = range(last)
    for i in count(2):
        if i * i >= last:
            break
        if primes[i] == 0:
            continue
        for j in count(2):
            if i * j >= last:
                break
            primes[i * j] = 0
    return [i for i in primes if i >= 2]

def length(a, b, primes):
    for n in count():
        if n * n + a * n + b not in primes:
            return n

def solve():
    primes = set(sieve(1000000))
    return max((length(a, b, primes), a * b)
               for a in xrange(-1000, 1001)
               for b in xrange(-1000, 1001))[1]

if __name__ == '__main__':
    print solve()
