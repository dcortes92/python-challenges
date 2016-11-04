# Sum of Primes

import sys

solution = 0
count = 0
number = 0

def isPrime(num):
    return all(num % i for i in xrange(2, num))

while (count < 1000):
    if (isPrime(number) and number > 1):
        solution += number
        count += 1
    number += 1

sys.stdout.write(str(solution) + '\n')
