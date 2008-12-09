from util import factorial, splitdigits

def iscurious(i):
    return i == sum(factorial(j) for j in splitdigits(i))

def curiousnumbers(last):
    return (i for i in xrange(10, last) if iscurious(i))

def solve():
    return sum(curiousnumbers(1000000))

if __name__ == '__main__':
    print solve()
