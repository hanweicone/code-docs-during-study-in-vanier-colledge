from functools import reduce
'''
Apply function of two arguments cumulatively to the items of iterable, 
from left to right, so as to reduce the iterable to a single value.
 For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
 calculates ((((1+2)+3)+4)+5). The left argument, x, 
 is the accumulated value and the right argument, y, 
 is the update value from the iterable. 
 If the optional initializer is present, it is placed before the items of the iterable in the calculation,
  and serves as a default when the iterable is empty. 
  If initializer is not given and iterable contains only one item, the first item is returned.
'''
# Roughly equivalent to:
def reduce1(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
        print(value)
    return value


def f(dict,value):
    if value in dict.keys():
        dict[value] += 1
    else:
        dict[value] = 1
    return dict

a=['a','b','a','c','b']

r = reduce(f, a, {'c':1})  # initializer = {'c':1}

print(r)
print(reduce1(f, a, {'c': 1}))  # check how reduce() works

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])  # (((1*2)*3)*4)
print(product)
product = reduce((lambda x, y: x * y), [1, 2, 3, 4], 10)  # ((((10*1)*2)*3)*4)
print(product)

