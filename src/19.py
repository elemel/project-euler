from datetime import date

def solve():
    return sum(date(year, month, 1).weekday() == 6
               for year in xrange(1901, 2001) for month in xrange(1, 13))

if __name__ == '__main__':
    print solve()

