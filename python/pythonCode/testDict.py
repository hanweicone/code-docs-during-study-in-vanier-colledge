import operator
# Items stored in a dictionary do not have any inherent order.
# The order they are printed out is entirely down to the hash values
# for each of the keys and the other items in the dictionary.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}  # no matter what order you give if it is same keys and values in dict,
d1 = {0: 0, 1: 2, 3: 4, 4: 3, 2: 1}  # print the same order automatically
print('Original dictionary : ', d)
print('Original dictionary : ', d1)
# notice:d.items() return a list with tuples of each keys and values
print('print d.items():', d.items())
sorted_d = sorted(d.items(), key=lambda x: x[0])  # sorted function return a list,did not change origin dict
print(type(sorted_d))
print(id(sorted_d))
print('Dictionary in ascending order by key  : ', sorted_d)
sorted_d = sorted(d.items(), key=lambda x: x[0], reverse=True)  # x[0] represent key, 'key:value'
print('Dictionary in descending order by key : ', sorted_d)
sorted_d = sorted(d.items(), key=lambda x: x[1])                # x[1] represent value
print('Dictionary in ascending order by value : ', sorted_d)
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print('Dictionary in descending order by value : ', sorted_d)

sorted_d = sorted(d.items(), key=operator.itemgetter(0))  # use itemgetter than lambda,same result
print(sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d)

# it is better to use tuple pair for dict() constructor
dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict2 = dict([['sape', 4139], ['guido', 4127], ['jack', 4098]])
dict3 = dict(zip(['sape', 'guido', 'jack'], [4139, 4127, 4098]))
print(dict1)
print(dict2)
print(dict3)

# ways to create dict
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)