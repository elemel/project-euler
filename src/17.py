from util import memoize

words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
         7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
         12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
         16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
         20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}

@memoize
def format(i):
    if i < 20:
        return words[i]
    elif i < 100:
        tens, ones = divmod(i, 10)
        result = words[tens * 10]
        if ones:
            result = '%s-%s' % (result, words[ones])
        return result
    elif i < 1000:
        hundreds, ones = divmod(i, 100)
        result = '%s hundred' % words[hundreds]
        if ones:
            result = '%s and %s' % (result, format(ones))
        return result
    else:
        return 'one thousand'

def countalpha(s):
    return sum(c.isalpha() for c in s)

def solve():
    return sum(countalpha(format(i)) for i in xrange(1, 1001))

if __name__ == '__main__':
    print solve()
