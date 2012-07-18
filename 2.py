def fib(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return fib(x-1) + fib(x-2)

x = 1
answer = 0
while fib(x) < 4000000:
    if fib(x) %2 == 0:
        answer += fib(x)
    x += 1


print answer
