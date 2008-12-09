from collections import defaultdict
from itertools import count

def readwords():
    f = open('words.txt')
    try:
        return f.read().strip().replace('"', '').split(',')
    finally:
        f.close()

def wordvalue(word):
    return sum(ord(letter) - ord('A') + 1 for letter in word)

def trianglenumbers(last):
    for n in count(1):
        t = n * (n + 1) // 2
        if t < last:
            yield t
        else:
            break

def solve():
    valuecounts = defaultdict(int)
    for word in readwords():
        valuecounts[wordvalue(word)] += 1
    maxvalue = max(valuecounts)
    numberset = set(trianglenumbers(maxvalue + 1))
    return sum(count for value, count in valuecounts.iteritems()
               if value in numberset)

if __name__ == '__main__':
    print solve()

