#pyton class
class MyClass:
    i= 12345 # class variable shared by all instances

    def f(self):
        return 'hello world'

x = MyClass()

print(x.i)
print(x.f())#the call x.f() is exactly equivalent to MyClass.f(x)
#constructor
class Dog:
    #tricks = []#mistaken use of a class variable, shared by all dogs
    def __init__(self,name,dog_type):
        self.name = name
        self.dog_type = dog_type
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter#after print,delete this attribute

#x.f is a method object, and can be stored away and called at a later time
xf = x.f
print(xf())

d = Dog('Marc','Lablado')
e = Dog('Buddy','Butterfly')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.name+' '+d.dog_type)
print(d.tricks)
print(e.tricks)