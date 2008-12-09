from itertools import count
from util import product

def solve():
    fraction = []
    for i in count(1):
        fraction.extend(str(i))
        if len(fraction) >= 1000000:
            break
    return product(int(fraction[10 ** i - 1]) for i in xrange(7))

if __name__ == '__main__':
    print solve()
