def solve():
    return sum(i for i in xrange(1, 1000) if i % 3 == 0 or i % 5 == 0)

if __name__ == '__main__':
    print solve()
