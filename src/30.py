def splitdigits(i):
    while i:
        yield i % 10
        i //= 10

def solve():
    return sum(i for i in xrange(10, 1000000)
               if i == sum(j ** 5 for j in splitdigits(i)))

if __name__ == '__main__':
    print solve()
