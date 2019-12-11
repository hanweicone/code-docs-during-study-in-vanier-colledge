def make_incrementor(n):
    return lambda x: x + n  # uses a lambda expression to return a function


f = make_incrementor(42)
print(f(1))


pairs = [(4, 'four'), (3, 'three'), (1, 'one'), (2, 'two') ]
pairs.sort(key=lambda pair: pair[0])
print(pairs)

students = [('john', 'C', 9), ('jane', 'B', 12), ('dave', 'A', 10)]
print(sorted(students, key=lambda student: student[2]))  # sorted return a new list,will not change original list
print(students)


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function())
print('-'*10)
print(my_function.__doc__)
