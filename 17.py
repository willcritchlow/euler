ones = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
teens = ('eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tens = ('ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

def print_ones(ones, prefix, output):
    for i in range(0,9):
        output.append(prefix + ones[i])
    return output

def print_teens(teens, prefix, output):
    for i in range(0,9):
        output.append(prefix + teens[i])
    return output

def print_under_100(ones, teens, tens, prefix, output):
    print_ones(ones, prefix, output)
    output.append(prefix + tens[0])
    print_teens(teens, prefix, output)
    for i in range(1,9):
        output.append(prefix + tens[i])
        print_ones(ones, prefix+tens[i], output)
    return output

output = []
output = print_under_100(ones, teens, tens, "", output)
for i in range(0,9):
    output.append(ones[i]+"hundred")
    output = print_under_100(ones, teens, tens, ones[i]+"hundredand", output)
output.append("onethousand")
print output[:30]
print len(output)

count = 0
for number in output:
    count = count + len(str(number))

print count
