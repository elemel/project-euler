from util import factoradic, joindigits

def solve():
    digits = range(10)
    indices = factoradic(1000000 - 1, len(digits))
    return joindigits(digits.pop(i) for i in indices)

if __name__ == '__main__':
    print solve()
