## clearly not my code.

def get_divisor_counts(start, length):
    """ Returns the number of divisors of every number from start up to, but
    not including, start+length.
    Requires: start >= 2
    """
    divisor_counts = [2]*length
    for d in xrange(2, (start+length-1)/2 + 1):
        for i in xrange(max(d*2-start, -start%d), length, d):
            divisor_counts[i] += 1
    return divisor_counts

def highly_composite_triangular_numbers():
    """ An infinite generator which outputs all highly composite triangular
    numbers, starting at T_1=1.
    """
    start = 0
    divisor_counts = [0, 1, 2, 2, 3, 2] #Divisor counts
    length = 6
    nd_max = 0 #Maximum number of divisors seen so far
    i = 1 #Current position in the array of divisor counts.
    while True:
        if i+1 >= length:
            start += length-1
            length *= 2
            divisor_counts = get_divisor_counts(start, length)
            i = 0
        n = (i+start)*(i+start+1)
        c = (n & -n).bit_length()
        nd = divisor_counts[i]*divisor_counts[i+1]*(c-1)/c
        if nd > nd_max:
            yield i+start, n/2, nd
            nd_max = nd
        i += 1

def find_hctn(req=5000):
    for i, n, nd in highly_composite_triangular_numbers():
        if nd > req:
            return i, n, nd

if __name__ == '__main__':
    import time
    start = time.clock()
    count = 1
    for i, n, nd in highly_composite_triangular_numbers():
        print '({:02}) With {:5} divisors, T_i={:15} (i={:8}) [{:7.3f}s]'.format(
            count, nd, n, i, time.clock()-start)
        count += 1
