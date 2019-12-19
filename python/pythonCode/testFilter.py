'''
 filter creates a list of elements for which a function returns true.
 Here is a short and concise example:
'''

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))  # use list() to convert a filter object to a list
print(less_than_zero)