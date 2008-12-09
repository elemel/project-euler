def solve():
    return sum(xrange(1, 101)) ** 2 - sum(i ** 2 for i in xrange(1, 101))

if __name__ == '__main__':
    print solve()
