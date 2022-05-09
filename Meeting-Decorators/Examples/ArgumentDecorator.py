# now what if I want to have a function that takes some parameters?

# for example 

def function(function_parameter):
    print(function_parameter)

function("sus")
# this function wont work with the simple decorator we made before,
# because the "wrapper" doesnt account for the function parameter

# lets fix that by adding a parameter for the "wrapper" that will allow the function to work 

def decorator(func):

    def wrapper(wrapper_parameter):
        print("decoration begins")
        func(wrapper_parameter)
        print("decoration ends")

    return wrapper

@decorator
def function(function_parameter):
    print(function_parameter)

function("sus")

# great now it works
# but you might have noticed a small issue
# What if the function being decorated has more than 1 parameter?
# it wont work because we only accept one in this decorator

# So in order to make our decorator work on all functions regardless of their argument lets add
# "*args" and "**kwargs" as parameters
# these are universal in python and basically accept any value in the "*args" and any key-value (i.e. dictionary) in the "**kwargs"

def decorator(func):

    def wrapper(*args,**kwargs):
        print("decoration begins")
        func(*args,**kwargs)
        print("decoration ends")

    return wrapper


# lets test it with a function with 2 arguments

@decorator
def multi_function(function_parameter1, function_parameter2):
    print(f"{function_parameter1} {function_parameter2}")

multi_function("red", "sus")