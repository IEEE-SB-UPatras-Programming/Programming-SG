# Since we now got the function basics out of the way lets begin

# lets make a simple function
def function():
    print("function")


# lets make a simple decorator that will print out when the function begins and ends

def decorator(func):

    def wrapper():
        print("decoration begins")
        func()
        print("decoration ends")

    return wrapper

# now lets pass our original function through the docarator to get the decorated function
decorated_func = decorator(function)
decorated_func()

# now we have added extra functionality without messing with our original function
function()

# but what if we want to use only the decorated function
# if instead of the decorated_function we store the new function in the old name
# we will change the functionality of function()
function = decorator(function)
function()

# it may be weird if you are seeing this for the first time, but remember "function" is just a pointer to a function
# and we just change it to another function whilst keeping the same name

# Now since we got that lets make our life easier and instead of doing line 29 over and over for every function,
# we will just use the @decorator

# lets get our function from before and add the decorator

@decorator
def sus():
    print("vented")

sus()

# great our decorator works, now lets make ANOTHER!

# this decorator will be probably the most usefull everywhere since it can be used to debug a program
# this decorator will calculate the time it took to run a function
import time

def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f"function duration :{duration}")
    
    return wrapper

# now lets make a function to measure and add the decorator

@duration_decorator
def bed_time():
    print("going to bed!")
    time.sleep(1)

bed_time()

# great now we now how long the function likes to sleep , 
# but i also want to know when starts going to bed and when it gets up

# and now for a party trick, instead of rewriting the function lets just use our first decorator! (0.o)

@decorator
@duration_decorator
def bed_time():
    print("going to bed!")
    time.sleep(1)

bed_time()
# Nani??!!!!
# Cool huh?, the decorator doesnt care if the function is decorated or whatever
# we just used the output of the "duration_decorator" as the input for the "decorator"
# and we can do it because the function is just a pointer


# CAN WE GO FURTHER?

# lets make multiple functions run from 1 function! 

# first lets make a decorator to double the function

def double_decorator(func):
    def wrapper():
        func()
        func()
    
    return wrapper

# now lets make 2 functions go to sleep from 1 function call

@double_decorator
@decorator
@duration_decorator
def bed_time():
    print("going to bed!")
    time.sleep(1)

bed_time()

# AMAZING WOW
# small sidenote: if you noticed the order from top to bottom matters for the end result