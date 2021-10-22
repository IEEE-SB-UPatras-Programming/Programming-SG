import ast
import struct

# https://evanw.github.io/float-toy/
# https://www.rapidtables.com/convert/number/decimal-to-binary.html

def StringCharBaseTwo(s):

    floatNums = [ ]

    for c in s:
        
        binaryRepresentation = format( ord(c), 'b').rjust(8, '0')
        floatNums.append( binaryRepresentation )

    for i in range(0, len(floatNums), 4):
        
        completeFloatList = list( floatNums[i:i+4] )
        completeFloatList.reverse()

        completeFloatBinaryRepresentation =  "".join(completeFloatList).rjust(32, '0')

        # print(completeFloatBinaryRepresentation)

        completeFloat = int( completeFloatBinaryRepresentation, 2 )

        f = struct.unpack('f', struct.pack('I', completeFloat))[0]

        print(f)


StringCharBaseTwo("string")
