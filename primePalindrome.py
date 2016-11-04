# Prime Palindrome

import sys

numberList = []
solution = 0

def isPrime(num):
    return all(num % i for i in xrange(2, num))

def isPalindrome(num):
    return str(num) == str(num)[::-1]

for num in range(0, 1000):
    if (isPrime(num) and isPalindrome(num)):
        solution = num

sys.stdout.write(str(solution) + '\n')
