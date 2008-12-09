from util import reversedigits

def solve():
    result = 0
    for i in xrange(999, 99, -1):
        for j in xrange(999, 99, -1):
            if i * j <= result:
                break
            if i * j == reversedigits(i * j):
                result = i * j
    return result

if __name__ == '__main__':
    print solve()

