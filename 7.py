max = 200000
sieve = range(2, max)

i = 2
while i != 0:
    for j in range(i*2,max,i):
        sieve[j - 2] = 0
    remaining_sieve = sorted(sieve)
    try:
        i = min(x for x in remaining_sieve if x > i)
    except:
        i = 0

primes = [x for x in sieve if x != 0]
print "found %s primes - the largest is %s" % (len(primes), primes[-1])
print "the sixth prime is %s" % primes[5]
print "the 10,001st prime is %s" % primes[10000]
