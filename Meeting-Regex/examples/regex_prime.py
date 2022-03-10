import re
import sys

def is_prime(n):
    return not re.match(r'^.?$|^(..+?)\1+$', '1'*n)

print(is_prime(int(sys.argv[1])))
