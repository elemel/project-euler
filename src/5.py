from util import factor, product
from collections import defaultdict

def solve():
    max_factors = defaultdict(int)
    for i in xrange(1, 21):
        factors = defaultdict(int)
        for j in factor(i):
            factors[j] += 1
        for k in factors:
            max_factors[k] = max(max_factors[k], factors[k])
    return product(k ** v for k, v in max_factors.iteritems())

if __name__ == '__main__':
    print solve()
