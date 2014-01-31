print "**Brett's factorial calculator**"
num = input('Enter a number greater than 1: ')

factorial = 1
tempint = 2

while tempint <= num :
    factorial = factorial * tempint
    tempint += 1

print '{0}! is: {1}' .format(num, factorial)
