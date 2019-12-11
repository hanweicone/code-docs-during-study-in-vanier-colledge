t = 12345, 54321, 'hello!'  # tuple without brackets
# t[0] = 8888 # Tuples are immutable
t1 = ('singel')  # if not use comma ,even use brackets,t1 is still a string,not tuple
print(t1)
print(type(t1))
t2 = 'singel',  # use a comma,if just one element in tuple
print(t2)
print(type(t2))
t3 = ('single',)
print(t3)
print(type(t3))

t4 = ()  # empty tuple
print(type(t4))

t5 = None
print(type(t5))
t6 = ''
print(type(t6))

t7 = ('a', 'b', 'c')
print(t7[:-1])
