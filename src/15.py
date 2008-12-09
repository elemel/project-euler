from util import memoize

@memoize
def solve(py=0, px=0, qy=20, qx=20):
    if py > qy or px > qx:
        return 0
    elif py == qy and px == qy:
        return 1
    else:
        return solve(py + 1, px, qy, qx) + solve(py, px + 1, qy, qx)

if __name__ == '__main__':
    print solve()

