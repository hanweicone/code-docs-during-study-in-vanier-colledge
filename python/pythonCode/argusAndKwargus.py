
# this is wrong function,if nested list level is more than 2,it will not cal the number
def total(*numbers):
    s = 0
    for x in numbers:
        if isinstance(x,int):
            s += x
        if isinstance(x,list):
            for y in x:
                if isinstance(y, int):
                    s +=y
    return s


# use recursive to calculate total of all int number pass by *argus
def caltotal(*numbers):  # notice convert between *argus and list
    n = []
    for x in numbers:
        n.append(x)  # convert *numbers to list n
    if len(n) == 0:
        return 0
    if isinstance(n[0], list):
        return caltotal(*n[0]) + caltotal(*n[1:])  # use list n as *argus with add * before it
    elif isinstance(n[0], int):
        return n[0] + caltotal(*n[1:])
    else:
        return 0 + caltotal(*n[1:]) # if n[0] is not int or list calculate as 0


def f(**d):
    if 'a' in d.keys() and 'b' in d.keys() and 'c' in d.keys():
        if isinstance(d['a'],int) and isinstance(d['b'],int) and isinstance(d['c'],int):
            return d['a']+d['b']+d['c']
        else:
            return 0
    else:
        return None


print(f(g=1,b=2,c=5,a=9))
print(total('a',1,2,[1,2,3,[2,4]]))  # use *argus
print(total(*['a',1,2,[1,2,3,[2,4]]]))  # use list as *argus by add *before this list
print(caltotal('a',1,2,[1,2,3,[2,4]]))  # use *argus
print(caltotal(*['a',1,2,[1,2,3,[2,4]]]))  # use list as *argus by add *before this list


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')

ll = ['python', 'eggs', 'test']

test_var_args('yasoob', *ll)  # use *before list to convert list to *argus
