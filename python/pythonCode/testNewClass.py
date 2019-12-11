class A(object):
    def __new__(cls):
        print('A __new__ called.')
        return super(A, cls).__new__(cls)

    def __init__(self):
        print('A __init__ called')


class B(A):
    def __new__(cls):
        print('B __new__ called.')
        return super(B, cls).__new__(cls)

    def __init__(self):
        print('B __init__ called')


a = A()
print(a)
b = B()
print(b)