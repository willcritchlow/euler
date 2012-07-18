max = 10000

def d(n):
    return sum([x for x in xrange(1,n) if n%x == 0])

amicable = []

for x in xrange(1,max+1):
    try:
        divisors = d(x)
        rev_divisors = d(divisors)
        if x == rev_divisors and x > divisors:
            print "divisors of %s are %s and divisors of %s are %s" % (x,divisors,divisors,rev_divisors)
            amicable.append(x)
            amicable.append(divisors)
    except:
        print "out of range"

print amicable
print sum(amicable)
