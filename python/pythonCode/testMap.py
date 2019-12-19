# applies a function(square) to all the items in an input_list
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)

# use map and lambda
squared = list(map(lambda x: x**2, items))
print(squared)


def sq(x):
    return x**2


# use map and function
print(list(map(sq, items)))


def multiply(x):
    return (x*x)


def add(x):
    return (x+x)


'''
Most of the times we use lambdas with map so I did the same.
Instead of a list of inputs we can even have a list of functions!
'''
funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda func: func(i), funcs))
    print(value)