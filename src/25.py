from util import fibonacci

def solve():
    for i, term in enumerate(fibonacci()):
        if len(str(term)) >= 1000:
            return i + 1

if __name__ == '__main__':
    print solve()
