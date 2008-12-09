from itertools import count as _count

def sieve(last):
    primes = range(last)
    for i in _count(2):
        if i * i >= last:
            break
        if primes[i] == 0:
            continue
        for j in _count(2):
            if i * j >= last:
                break
            primes[i * j] = 0
    return list(prime for prime in primes if prime >= 2)

def memoize(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

def product(iterable):
    """
    >>> product([304, 152, 5914])
    273274112
    """
    result = 1
    for x in iterable:
        result *= x
    return result

def factorial(n):
    return product(xrange(2, n + 1))    

def splitdigits(i, base=10):
    """
    >>> splitdigits(0)
    []
    >>> splitdigits(13)
    [1, 3]
    """
    digits = []
    while i:
        digits.append(i % base)
        i //= base
    digits.reverse()
    return digits

def joindigits(digits, base=10):
    """
    >>> joindigits([])
    0
    >>> joindigits([1, 3])
    13
    """
    i = 0
    for j in digits:
        i *= base
        i += j
    return i

def reversedigits(i, base=10):
    """
    >>> reversedigits(0)
    0
    >>> reversedigits(9)
    9
    >>> reversedigits(13)
    31
    >>> reversedigits(80891492769135132)
    23153196729419808L
    """
    j = 0
    while i:
        j *= base
        j += i % base
        i //= base
    return j

def factoradic(i, length=None):
    result = []
    radix = 1
    while i:
        result.append(i % radix)
        i //= radix
        radix += 1
    result.reverse()
    if length is not None:
        result = ([0] * length + result)[-length:]
    return result

def factor(i):
    """
    >>> factor(11)
    [11]
    >>> factor(28)
    [2, 2, 7]
    >>> factor(49)
    [7, 7]
    """
    result = []
    j = i
    for prime in sieve(int(i ** 0.5) + 2):
        while j % prime == 0:
            j //= prime
            result.append(prime)
    if j != 1:
        result.append(j)
    return result

def nthprime(n):
    """
    >>> nthprime(0)
    2
    """
    last = max(1, n * 10)
    primes = []
    while len(primes) <= n:
        last *= 10
        primes = sieve(last)
    return primes[n]

def fibonacci(i=1, j=1):
    while True:
        yield i
        i, j = j, i + j

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

