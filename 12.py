def triangle(n):
    return sum(range(1,n+1))

def factors(n):
    return len([x for x in range(1,n+1) if n%x == 0])

x = 1
while True:
    if factors(triangle(x)) > 500:
        print x
        print triangle(x)
        print factors(triangle(x))
        exit()
    x = x+1
