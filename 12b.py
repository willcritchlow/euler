def triangle(n, already_found):
    if n == 1:
        return 1, already_found
    try:
        tri = already_found[n]
    except:
        tri_minus, already_found = triangle(n-1, already_found)
        tri = tri_minus + n
        already_found.append(tri)
    return tri, already_found

def prime_factors(n, cache, primes):
    "Returns all the prime factors of a positive integer"
    factors = []
    orig_n = n
    d = 0
    while (n > 1):
        try:
            for f in cache[n]:
                factors.append(f)
            return factors, cache
        except:
            prime = primes[d]
            while (n%prime==0):
                factors.append(prime)
                n /= prime
            d = d + 1
    cache[orig_n] = factors
    return factors, cache

def find_exponents(array):
    current = 0
    exponent = 1
    exponents = []
    for x in array:
        if x == current:
            exponent = exponent + 1
        else:
            if current != 0:
                exponents.append(exponent)
            current = x
            exponent = 1
    exponents.append(exponent)
    return exponents

def num_factors(exponents):
    base = 1
    for e in exponents:
        base = base * (e + 1)
    return base

cache = {}
max = 2000000
sieve = range(2, max)

i = 2
while i != 0:
    for j in range(i*2,max,i):
        sieve[j - 2] = 0
    try:
        i = min(x for x in sieve if x > i)
    except:
        i = 0

primes = [x for x in sieve if x != 0]

x = 1
already_found = []
max_f = 0
max_x = 0
while True:
    tri, already_found = triangle(x, already_found)
    factors, cache = prime_factors(tri, cache, primes)
    f = num_factors(find_exponents(factors))
    if f > 500:
        print x
        print tri
        print f
        exit()
    if f > max_f:
        max_f = f
        max_x = x
    x = x+1
    if x%100 == 0:
        print "passing through %s" % x
        print "current max factors: %s, at: %s" % (max_f, max_x)
