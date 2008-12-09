from util import factorial

def solve():
    return sum(int(c) for c in str(factorial(100)))

if __name__ == '__main__':
    print solve()

