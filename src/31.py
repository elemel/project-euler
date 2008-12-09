from util import memoize

coins = [1, 2, 5, 10, 20, 50, 100, 200]

@memoize
def next_coin(coin):
    try:
        return coins[coins.index(coin) + 1]
    except IndexError:
        return 0

@memoize
def solve(pennies=200, coin=1):
    if not coin:
        return pennies == 0
    return sum(solve(pennies - count * coin, next_coin(coin))
               for count in xrange(pennies // coin + 1))

if __name__ == '__main__':
    print solve()
