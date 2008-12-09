from util import fibonacci

def solve():
    result = 0
    for i in fibonacci(1, 2):
        if i > 4000000:
            return result
        elif i % 2 == 0:
            result += i

if __name__ == '__main__':
    print solve()
