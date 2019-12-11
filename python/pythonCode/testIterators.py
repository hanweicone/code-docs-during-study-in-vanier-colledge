# Behind the scenes, the for statement calls iter() on the container object
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
"""
for line in open("myfile.txt"):
    print(line, end='')
"""
s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) #stop


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
# Define an __iter__() method which returns an object with a __next__() method.
    # If the class defines __next__(), then __iter__() can just return self

    def __iter__(self):
        return self

    def __next__(self):  # next method of reverse iterator
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


rev = Reverse('spam')
print(next(iter(rev)))  # iter and next function actually call the Class function of Reverse
print('---------')
for char in rev:  # next is already become -2,so print from -2
    print(char)
print('--------')
for char in reverse('golf'):
    print(char)