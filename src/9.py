def solve():
    for a in xrange(1, 1001):
        for b in xrange(1, 1001):
            c = 1000 - a - b
            if a < b < c and a ** 2 + b ** 2 == c ** 2:
                return a * b * c
