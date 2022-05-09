# I am trying to make a script to type fast in amogus

# this function says what was sus
def sus():
    print("vented")

sus()
# saying just sus doesnt help a lot other to understand
# other need more context to get what i am trying to say

# so i make a wraper for my function that adds context, so i dont have to rewrite it
def wrapper(function):
    print("red")
    function()
    print("in electrical")

# now everyone can understand me
wrapper(sus)


# But what if red did something else that was sus?

# thankfully my wrapper can take any function that says what red did

# so lets make a function that will anyting be sussy

def sus_maker():

    def new_sus():
        print("followed me")

    return new_sus

followed = sus_maker()

# lets see if it works
followed()

wrapper(followed)
