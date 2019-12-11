t  = [1, [2, [4 ] , [5, [], []]], [5,[6]], []]

def isInTree(tree, element):
    if len(tree)==0:
        return False
    '''
    return tree[0]==element or isInTree(tree[1],element) or isInTree(tree[2],element) 
    '''
    if tree[0]==element: return True
    for i in range(1,len(tree)):
        if isInTree(tree[i],element): return True
    return False


print(isInTree(t, 6))
