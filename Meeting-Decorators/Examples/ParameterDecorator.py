# Now what if we want to make a decorator that takes some parameters

# lets make an example

def function():
    print("function")

for i in range(3):
    function()

# this is kind of repetitive (get it?) , what if we made a decorator that would repeat a function the number of time we want?

# so lets make a decorator that will accept some arguments
# this is kind of weird so pay attention

# first lets make a decorator that will receive the argument(this is the decorator we will call)

def repetition_decorator(repetitions):

    # next we will create the actual decorator that accepts the function

    def decorator(func):

        # now we continue as expected
        def wrapper():
            for i in range(repetitions):
                func()

        return wrapper

    # finally we will return the actual decorator
    return decorator


@repetition_decorator(3)
def function():
    print("function")

function()

# Wow it actually works
# but despite it working we feel like we violated something

# so lets se whats going on in detail, by writing it the "traditional way" (without the @)

function = repetition_decorator(3)(function)

# First remember the simple Functions we first made, we said that we can return new functions we create

# So firstly the "repetition_decorator(repetitions)" is a function that creates another function (just like the one in SimpleFunction.py)
# with repetitions being a parameter that changes the function it creates

# After we give it the repetitions parameter it will create a new function (the actual decorator in our case) that repeats the "func" ,
# which is a parameter for the new function

# So after all we werent violating anything, but is dure was confusing at first glance