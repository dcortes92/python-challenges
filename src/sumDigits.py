# Sum of digits
# input file: sumDigits.txt

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test:
            number = int(test)
            solution = 0
            while (number > 0):
                digit = number % 10
                solution += digit
                number = number / 10
            sys.stdout.write(str(solution) + '\n')
