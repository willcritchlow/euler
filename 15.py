#Until you hit an edge, there are 2 choices at every move

#in the 2x2, you hit an edge in 3 goes at most

#in a 3x3 you hit an edge in 5 goes at most

#in a 4x4 you hit an edge in 7 goes at most

#You hit an edge in at most 20x2-1 = 39 goes (and a minimum of 20 goes)

#Once you have hit an edge, the options collapse. Suppose that 

#So there are 2^39 moves except the ones where you hit an edge early collapse

#in a 3x3 you hit the edge immediately in 2 ways
#you hit the edge 




#f_(n-1) * 2 + 2

def routes(a,b, cache):
    if a == b == 1:
        return 2, cache
    elif a == 1:
        return b+1, cache
    elif b == 1:
        return a+1, cache
    else:
        try:
            answer = cache[a][b]
        except:
            answer1, cache = routes(a,b-1, cache)
            answer2, cache = routes(a-1,b, cache)
            answer = answer1 + answer2
            try:
                cache[a][b] = answer
            except:
                cache[a] = {}
                cache[a][b] = answer
            if a == b:
                print "working on %s x %s" % (a,b)
        return answer, cache

cache = {}
print routes(2,2, cache)[0]
print routes(3,3, cache)[0]
print routes(2,1, cache)[0]
print routes(20,20, cache)[0]
