# Fibonacci series
# input file: fibN.txt

import sys

def fib(n):
    if (n == 1):
        return 1
    if (n < 1):
        return 0
    else:
        return fib(n-1) + fib(n-2)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test:
            number = int(test)
            solution = fib(number)
            sys.stdout.write(str(solution) + '\n')
