
str1 = 'abcba'

'''
Ever since Python 1.4, the slicing syntax has supported an optional third ``step'' or ``stride'' argument. For example,
 these are all legal Python syntax: L[1:10:2], L[:-1:1], L[::-1]. 
 This was added to Python at the request of the developers of Numerical Python, which uses the third argument extensively.
  However, Python's built-in list, tuple, and string sequence types have never supported this feature, 
  raising a TypeError if you tried it. Michael Hudson contributed a patch to fix this shortcoming.
'''
print(str1 == str1[::-1])
print(str1[::-1])


def ispalindrome(word):

    '''Return True if the given word is a palindrome.'''  # use docstring
    return word == word[::-1]

print(repr(ispalindrome.__doc__))