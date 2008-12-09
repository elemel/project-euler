from itertools import count

def turn_right(dy, dx):
    return dx, -dy

def spiral_walk(dy, dx):
    while True:
        for length in count(1):
            for line in xrange(2):
                for step in xrange(length):
                    yield dy, dx
                dy, dx = turn_right(dy, dx)

def generate_spiral(size):
    grid = [[0] * size for y in xrange(size)]
    y = x = size // 2
    for i, (dy, dx) in zip(xrange(size ** 2), spiral_walk(0, 1)):
        grid[y][x] = i + 1
        y += dy
        x += dx
    return grid

def diagonal_indices(size):
    center = size // 2
    return ((y, x) for y in xrange(size) for x in xrange(size)
            if abs(y - center) == abs(x - center))

def solve():
    size = 1001
    grid = generate_spiral(size)
    return sum(grid[y][x] for y, x in diagonal_indices(size))

if __name__ == '__main__':
    print solve()
