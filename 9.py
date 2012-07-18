from math import sqrt
squares = [x**2 for x in range(1,1000)]

for c in range(1,1000):
    aplusb = 1000 - c
    bs = [x for x in range(1,aplusb/2)]
    a_s = []
    for b in bs:
        a_s.append(aplusb - b)

    for a in a_s:
        for b in bs:
            c_2 = a**2 + b**2
            if c_2 in squares:
                c = squares.index(c_2)+1
                if a + b + c == 1000:
                    print a*b*c
                    print "%s %s %s" % (a,b,c)
