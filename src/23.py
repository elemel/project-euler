import sys

def properdivisors(i):
    return (j for j in xrange(1, i // 2 + 1) if i % j == 0)

def isabundant(i):
    return sum(properdivisors(i)) > i
    
def abundantnumbers(last=sys.maxint):
    return (i for i in xrange(12, last) if isabundant(i))

def solve():
    last = 28124
    alist = list(abundantnumbers(last))
    nlist = range(last)
    for i in alist:
        try:
            for j in alist:
                nlist[i + j] = 0
        except IndexError:
            pass
    return sum(nlist)

if __name__ == '__main__':
    print solve()
