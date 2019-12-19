basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # duplicates have been removed in set
print('orange' in basket)  # fast membership testing

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')  # transform a string into character set
b = set('alacazam')
print(a)  # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
# if not use operation '|' we need do below
c = list(a)
c.extend(list(b))
print(set(c))

print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both
print('-'*20)
# set comprehensions
print({x for x in 'abracadabra' if x not in 'alacazam'})  # a - b
print(set('abracadabra').difference(set('alacazam')))  # a - b
print({x for x in 'abracadabra' if x in 'alacazam'})  # a & b
print(set('alacazam').intersection(set('abracadabra')))  # a & b

def get_duplicates(list):
    duplicates = []
    for value in list:
        if list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)

    return duplicates


def get_duplicates1(list):
    duplicates = set([x for x in list if list.count(x) > 1])
    return duplicates


l1 = [1, 1, 2, 2, 3, 5, 6, 7]
print(get_duplicates(l1))
print(get_duplicates1(l1))



