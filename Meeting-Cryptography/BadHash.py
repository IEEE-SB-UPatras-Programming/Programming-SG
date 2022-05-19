def hashCode(s):
    k = 0 
    for c in s:
        k = ( 7 * k + 3 * ord(c) ) % 61
    return k


