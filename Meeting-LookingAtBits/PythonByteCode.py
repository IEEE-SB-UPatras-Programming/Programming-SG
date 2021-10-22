import inspect
import dis

class MyClass():

    def __init__(self, val):

        self.val = val

        self.sister = None
    
    def add(self, node):

        self.sister = node

def test():

    a = MyClass(12)
    b = MyClass(13)

    a.add(b)

def func(a, b):

    return a + b

sourceCode = inspect.getsource(test)


print("SOURCE CODE: \n", sourceCode)
print("BYTE CODE: \n", dis.Bytecode(test).dis())


import timeit

duration = timeit.Timer(test).timeit(1000000)

print("Total Time: {}".format(duration))
