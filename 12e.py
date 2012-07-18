from math import sqrt

triangle = 0
i = 0
while True:
    i += 1
    triangle += i
    f = 0
    for n in xrange(1,int(sqrt(triangle))):
        if triangle%n == 0:
            f += 2
        if f > 500:
            print "we win"
            print i
            print triangle
            exit()
