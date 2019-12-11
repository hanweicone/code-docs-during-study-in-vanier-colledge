from binarytree import Node


def lists_represent_tree(r):
    return [r, [], []]


def insert_left(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root


def insert_right(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, newVal):
    root[0] = newVal


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


# convert Node tree to list of lists tree
def tree_to_list(root):
    if root == None:
        return []
    return [root.value, tree_to_list(root.left), tree_to_list(root.right)]


r = lists_represent_tree(3)
insert_left(r,4)
insert_left(r,5)
insert_right(r,6)
insert_right(r,7)
l = get_left_child(r)
print(l)

set_root_val(l,9)
print(r)
insert_left(l,11)
print(r)
print(get_right_child(get_right_child(r)))
[3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]

r1 = lists_represent_tree(3)
insert_left(r1, 4)
insert_right(r1, 5)
insert_left(getLeftChild(r1), 6)
insert_right(getLeftChild(r1), 7)
print(r1)

root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(6)
root.left.right = Node(7)
root.right.left = Node(8)
root.right.right = Node(9)
print(treeToList(root))
[3, [4, [6, [], []], [7, [], []]], [5, [8, [], []], [9, [], []]]]