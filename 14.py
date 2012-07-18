def iterative(n):
    if n%2 == 0:
        return n / 2
    else:
        return 3*n + 1

def chain(n,count,cache):
    if n == 1:
        return 1, count, cache
    else:
        try:
            answer, count = cache[n]
        except:
            answer, count, cache = chain(iterative(n), count,cache)
            count = count + 1
            cache[n] = (answer, count)
        return answer, count, cache

found = {}
max_chain = 0
max_chain_x = 0
#import pdb; pdb.set_trace()
for x in range(1,1000001):
    temp, this_chain, found = chain(x,1,found)
    if this_chain > max_chain:
        max_chain = this_chain
        max_chain_x = x
    if x%1000 == 0:
        print "passing through %s" % x
        print "max chain so far: %s at %s" % (max_chain, max_chain_x)

print max_chain
print max_chain_x
