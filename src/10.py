from util import sieve

def solve():
    return sum(sieve(2000000))

if __name__ == '__main__':
    print solve()
