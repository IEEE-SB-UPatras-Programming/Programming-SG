def hashCode(s):
    k = 0 
    for c in s:
        k = ( 7 * k + 3 * ord(c) ) % 61
    return k


# solution

from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]
