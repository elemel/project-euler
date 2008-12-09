def memoize(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

def properdivisors(i):
    return (j for j in xrange(1, i // 2 + 1) if i % j == 0)

@memoize
def sumproperdivisors(i):
    return sum(properdivisors(i))

def isamicable(i):
    j = sumproperdivisors(i)
    return j != i and sumproperdivisors(j) == i
    
def solve():
    return sum(i for i in xrange(1, 10000) if isamicable(i))

if __name__ == '__main__':
    print solve()
