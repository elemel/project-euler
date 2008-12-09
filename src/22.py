def score(i, name):
    return (i + 1) * sum(ord(c) - ord('A') + 1 for c in name)

def solve():
    names = open('names.txt').read().replace('"', '').split(',')
    names.sort()
    return sum(score(i, name) for i, name in enumerate(names))

if __name__ == '__main__':
    print solve()
