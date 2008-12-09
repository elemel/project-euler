from util import memoize

triangle = [[int(s) for s in line.split()]
           for line in open('triangle.txt').read().strip().splitlines()]
height = len(triangle)


@memoize
def solve(y=0, x=0):
    if y >= height:
        return 0
    return triangle[y][x] + max(solve(y + 1, x), solve(y + 1, x + 1))
