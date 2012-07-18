def palindrome(x):
    return str(x) == str(x)[::-1]

a = 999
b = 999

numbers = [a*b for a in range(100,999) for b in range(100,999)]

big_numbers = sorted(numbers, reverse=True)

for num in big_numbers:
    if palindrome(num):
        print num
        exit()
