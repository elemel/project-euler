import sys
from util import memoize

sys.setrecursionlimit(1000)

@memoize
def length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + length(n // 2)
    else:
        return 1 + length(3 * n + 1)

def solve():
    return max((length(n), n) for n in xrange(1, 1000000))[1]

if __name__ == '__main__':
    print solve()

