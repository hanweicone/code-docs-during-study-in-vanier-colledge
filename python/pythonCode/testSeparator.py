def concat(*args1, sep="/"):
    return sep.join(args1)


print(concat('hello', 'world', 'hello'))


def test_yield(n):
    x = 0
    while x <= n:
        yield x
        x += 1


for i in test_yield(10):
    print(i)


print(list(range(3, 6)))           # normal call with separate arguments
args = [3, 10, 2]
print(list(range(*args)))        # call with arguments unpacked from a list


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

print(parrot(**d))