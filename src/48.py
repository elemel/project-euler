def solve():
    return int(str(sum(i ** i for i in xrange(1, 1001)))[-10:])

if __name__ == '__main__':
    print solve()
