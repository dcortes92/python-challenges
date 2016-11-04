# Reverse Words
# input file: reverseWords.txt

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test:
            test = test.rstrip()
            arr = test.split(' ')[::-1]
            solution = ' '.join(arr)
            sys.stdout.write(solution + '\n')
