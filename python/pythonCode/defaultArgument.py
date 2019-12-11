# coding=utf-8

# he most useful form is to specify a default value for one or more arguments.
# This creates a function that can be called with fewer arguments than it is defined to allow
def ask_ok(prompt, retries=3, reminder='Please try again!'):
    while retries > 0:
        ok = input(prompt)  # python 2.7 need to use raw_input
        if ok in ('y', 'ye', 'yes'):  # in keyword. This tests whether or not a sequence contains a certain value
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries <= 0:
            raise ValueError('invalid user response')
        print(reminder + 'you have ' + str(retries) + ' enter times')


ask_ok('want quit?')
ask_ok('do you want to quit?', 4, 'just use yes or no! ')
i = 5


# The default values are evaluated at the point
# of function definition in the defining scope
def f(arg=i):
    print(arg)


i = 6  # The default value is evaluated only once
f()


# when default is a mutable object such as a list, dictionary, or instances of most classes.
# the following function accumulates the arguments passed to it on subsequent calls:
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# If you don’t want the default to be shared between subsequent calls
# you can write the function like this instead
def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f1(1))
print(f1(2))
print(f1(3))