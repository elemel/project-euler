from util import factor, product
from collections import defaultdict

def trianglenumber(n):
    return n * (n + 1) // 2

def divisorcount(n):
    factorcount = defaultdict(int)
    for i in factor(n):
        factorcount[i] += 1
    return product(count + 1 for count in factorcount.itervalues())

def solve():
    n = 1
    while divisorcount(trianglenumber(n)) < 500:
        print n, trianglenumber(n), divisorcount(n)
        n *= 2

if __name__ == '__main__':
    print solve()
