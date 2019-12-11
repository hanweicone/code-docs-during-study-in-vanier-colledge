import time
from itertools import permutations
import sys
# too much time use permutations
def replace_str(s):
    result = []
    if '*' not in s:
        print('string need contain "*"')
        return result
    pos = [pos for pos, char in enumerate(s) if char == '*']
    str_list = list(s)
    com_list = ['a']*len(pos)
    com_list.extend(['b']*len(pos))
    perm = permutations(com_list, len(pos))
    replace_charset = set(perm)
    for x in replace_charset:
        for i in range(len(pos)):
            str_list[pos[i]] = x[i]
        result.append(''.join(str_list))
    return result


def rec_replace_str(s, l1):
    if '*' not in s:
        l1.append(s)
        return
    rec_replace_str(s.replace('*', 'a', 1), l1)
    rec_replace_str(s.replace('*', 'b', 1), l1)


str1 = 'x*y*z*f'
str2 = 'x'+'*'*4+'y'+'*'*4  # the maximum recursion depth in Python is 997
# when has 8 *,function replace_str takes 42 seconds,when more then 8,it is very slow,but recursion way is much faster
time01 = time.time()
list1 = replace_str(str2)
time02 = time.time()
print(str(time02-time01))
str3 = 'x'+'*'*12+'y'+'*'*12  # takes 13 seconds,if more cause memory error
time03 = time.time()
list2 = []
rec_replace_str(str3, list2)
time04 = time.time()
print(str(time04-time03))

# sys.setrecursionlimit(2000)
# str3 = 'x'+'*'*1000+'y'+'*'*400
# time05 = time.time()
# list2 = rec_replace_str(str2)
# time06 = time.time()
# print(str(time06-time05))