def triangle(n, already_found):
    if n == 1:
        return 1, already_found
    try:
        tri = already_found[n]
    except:
        tri_minus, already_found = triangle(n-1, already_found)
        tri = tri_minus + n
        already_found.append(tri)
    return tri,already_found

def factors(n):
    return len([x for x in range(1,n+1) if n%x == 0])

x = 1
already_found = []
max_f = 0
while True:
    tri,already_found = triangle(x, already_found)
    f = factors(tri)
    if f > 500:
        print x
        print tri
        print f
        exit()
    if f > max_f:
        max_f = f
    x = x+1
    if x%100 == 0:
        print "passing through %s" % x
        print "current max factors: %s" % max_f
