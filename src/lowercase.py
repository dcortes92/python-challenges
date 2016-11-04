# Lowercase
# input file: lowercase.txt

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test:
            sys.stdout.write(test.lower())
