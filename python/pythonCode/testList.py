from collections import deque
from math import pi
l1 =[]
l1.append(1)
l1.append([2, 3])  # append a list of [2, 3] to l1 list
print(l1)
l1.extend([4, 5])  # Extend the list by appending all the items from the iterable
print(l1)
a = set('abracadabra')  # transform a string into character set
b = set('alacazam')
l8 = list(a)
print(l8)
l9 = list(b)
# l8 = l8.extend(l9) #not work,extend() just modify and return None
l8.extend(l9)
print(l8)
l1.remove([2, 3])
print(l1)
print(l1.pop())
print(l1)
l1.clear()  # Equivalent to del a[:]
l1.extend([1, 2, 3, 4])
print(l1)
del l1[:]  # remove an item from a list given its index instead of its value
print(l1)
l1.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2])
print(l1.index(5))
print(l1.count(1))
l1.sort(reverse=True)
print(l1)
print(id(l1))
l2 = l1.copy()
print(id(l2))
print(l2)

l3 = [1, 2, 3]
queue = deque(l3)  # queue fifo
print(queue)
print(queue.popleft())
print(queue)


# List Comprehensions provide a concise way to create lists
def sqrt(x):
    return x**2


square = list(map(lambda x: x**2, range(10)))
print(square)
square1 = [x**2 for x in range(10)]
print(square1)
# print([lambda x: x*2 for x in range(10)]) # can't use lambda here
print([sqrt(x) for x in range(10)])
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)
# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_vec =[]
for i in vec:
    for x in i:
        new_vec.append(x)
print(new_vec)
print([num for i in vec for num in i])
print('-'*20)
# List comprehensions can contain complex expressions and nested functions
print([str(round(pi, i)) for i in range(1, 6)])


#  transpose rows and columns
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# use nested list comprehension
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])  # partly use list comprehension
print(transposed)

# not use list comprehension
transposed1 = []
for i in range(4):
    transposed_row =[]
    for x in matrix:
        transposed_row.append(x[i])
    transposed1.append(transposed_row)
print(transposed1)

# * call with arguments unpacked from a list
print(list(zip(*matrix)))

