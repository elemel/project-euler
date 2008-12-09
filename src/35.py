from util import sieve

primes = set(sieve(1000000))

def rotations(i):
    result = []
    s = str(i)
    for j in xrange(len(s)):
        result.append(int(s[j:] + s[:j]))
    return result

def circular(prime):
    r = set(rotations(prime))
    return len(r) == len(r & primes)

def solve():
    return sum(circular(prime) for prime in primes)

if __name__ == '__main__':
    print solve()
