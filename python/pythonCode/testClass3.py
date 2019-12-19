# class Rectangle(object):
#     name = 'Rectangle'
#
#     def __init__(self, length, width ):
#         self.length = length
#         self.width = width
#
#     def __str__(self):
#         return 'This is Rectangle with length {0} and width {1}.'\
#             .format(self.length,self.width)
#
#     def get_area(self):
#         return self.length * self.width
#
#     def get_permiter(self):
#         return 2 * self.length + 2 * self.width
#
#
# class Square(Rectangle):
#     name = 'Square'
#
#     def __init__(self, length):
#         super(Square,self).__init__(length,length)
#
#     def __str__(self):
#         return 'This is a square of {0}'.format(self.length)
#
#
# mySquare = Square(10)
# print(mySquare.get_permiter())
# print(mySquare.get_area())
#
#
# class A(object):
#     def __new__(cls):
#         print('A __new__ called.')
#         return super(A,cls).__new__(cls)
#
#     def __init__(self):
#         print('A __init__ called')
#
#
# class B(A):
#     def __new__(cls):
#         print('B __new__ called.')
#         return super(B,cls).__new__(cls)
#
#     def __init__(self):
#         print('B __init__ called')
#
#
# class C(B):
#     def __new__(cls):
#         print('C __new__ called.')
#         return super(C,cls).__new__(cls)
#
#     def __init__(self):
#         print('C __init__ called')
#
#
# class D(C):
#     def __new__(cls):
#         print('D __new__ called.')
#         return super(A,cls).__new__(cls)
#
#     def __init__(self):
#         print('D __init__ called')
#
#
# d = D()

'''
in python 3 all the calss is new class
'''
class A(object):
    """ this is class A for use ..."""  # docstring of class
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name +'('+str(self.id)+')'

    student_id = property(fset=set_id,fget=get_id, doc='Student Id')
    student_name = property(fset=set_name, fget=get_name, doc='Student Name')


a = A()
print(A.__doc__)
print(A.student_id.__doc__)  # get docstring of attribute student_id in class A
print(A.student_id.__doc__)
a.student_id = 101
a.student_name = 'John'
print(a.student_id)
print(a.student_name)



class A(object):
    @property
    def student_id(self):
        """Student Id"""  # docstring same as doc='Student Id' in property
        return self.id
    @student_id.setter
    def student_id(self, id):
        self.id = id
    @property
    def student_name(self):
        """Student Name"""
        return self.name +'('+str(self.id)+')'
    @student_name.setter
    def student_name(self, name):
        self.name = name
a = A()
a.student_id = 101
a.student_name = 'John'
print(a.student_id)
print(a.student_name)
