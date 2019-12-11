

# works fine
def is_in_list(t, v):
    # set flag to false,check v later,if v is contained,flag=true,
    # if check all the elements in list,there is no chance let flag set to true,
    # return false
    flag = False
    if isinstance(t, list):
        for x in t:
            if isinstance(x, list):  # if x is list,recursively use function
                if is_in_list(x, v):  # if this is true,means v is contain
                    flag = True
                    break
            else:
                if x == v:
                    flag = True
                    break
    else:
        if t == v:
            flag = True
    return flag


# not working good
# def isInTree(tree, element):
#     if len(tree) == 0:
#         return False
#     '''
#     return tree[0]==element or isInTree(tree[1],element) or isInTree(tree[2],element)
#     '''
#     # if tree[0]==element: return True
#     # in the sublist,if there is a number in index -1:1,
#     # will let tree[i] is a int,and when use isIntree()
#     # will use len(),than cause typeerror:type 'int' has no len()
#     if element in tree or element == tree:
#         return True
#     for i in tree:
#         if isInTree(i, element) or i == element:
#             return True
#     return False


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])  # equals return [S[0]] + flatten(S[1:])


# wrong function of flatten
# def flatten1(test_list):
#     if isinstance(test_list, list):
#         if len(test_list) == 0:
#             return []
#         first, rest = test_list[0], test_list[1:]
#         return flatten(first) + flatten(rest)
#     else:
#         return [test_list]


# use flatten function to check contain
def check_contain_by_flatten(list, value):
    if value in flatten(list):
        return True
    else:
        return False


t = [1, [2, [4], [5, [], []]], [5, [6]], [] ]
t1 = [1, [2, [4], [5, 9, [], []]], [5, [6]], [], 7]
print(is_in_list(t, 6))
print(is_in_list(t, 10))
print(is_in_list(t1, 7))
print(is_in_list(t1, 9))
print(is_in_list(t1, 10))
print(is_in_list([], 10))
print('-----------')
print(check_contain_by_flatten(t, 6))
print(check_contain_by_flatten(t, 10))
print(check_contain_by_flatten(t1, 7))
print(check_contain_by_flatten(t1, 9))
print(check_contain_by_flatten(t1, 10))
print(check_contain_by_flatten([], 10))
