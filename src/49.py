from util import sieve, splitdigits
from collections import defaultdict

def solve():
    
    primes = sieve(10000)
    perm_sets = defaultdict(set)
    for prime in primes:
        if prime >= 1000:
            perm_sets[frozenset(splitdigits(prime))].add(prime)

    for perms in perm_sets.itervalues():
        for x in perms:
            for y in perms:
                if x < y:
                    z = y + (y - x)
                    if z in perms and z not in (1487, 4817, 8147):
                        return int('%s%s%s' % (x, y, z))

if __name__ == '__main__':
    print solve()
