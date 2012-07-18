composite = 600851475143

for i in range(2,1000000):
    if composite % i == 0:
        composite = composite / i
        print "prime factor %s" % i
