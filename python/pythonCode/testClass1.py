# If the same attribute name occurs in both an instance and in a class,
# then attribute lookup prioritizes the instance
class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


# Function defined outside the class
# assigning a function object to a local variable in the class is also ok.
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


# Methods may call other methods by using method attributes of the self argument
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


c1 = C()
print(f1)
print(id(f1))
print(f1(c1, 1, 2))  # self parameter --c1
print(c1.f)
print(id(c1.f))
print(c1.f(1, 2))
print(c1.g)
print(id(c1.g))
print(c1.g())
print(c1.h)
print(id(c1.h))
print(c1.h())
