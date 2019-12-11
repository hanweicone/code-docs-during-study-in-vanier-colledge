# parrot function accepts one required argument (voltage) and three optional arguments (state, action, and type).
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end ='')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
"""
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

"""


def f(a):
    return a


def f1(a=1):  # keyword arguments form
    return a


def f1(a=''):
    return a


print(f(0))  # regular way to pass parameter
print(f(a=0))  # use keyword arguments to pass
# print(f(b=0)) # unexpected keyword argument 'b'
print(f1(1))
print(f1(a=1))
print(f1('hello'))
print(f1(a='hello'))
