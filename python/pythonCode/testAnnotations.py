def f(ham: str, eggs: str = 'eggs') -> str:  # after -> is function return type annotation
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


print(f('beef', 'spam'))
print('-'*20)


# use ':' like keyword parameter use '='
def f1(ham: str, eggs: str):  # without default parameter
    return ham + ' and ' + eggs


def f2(ham: str, eggs: str = 'eggs'):  # with default parameter
    return ham + ' and ' + eggs


print(f1('beef', 'spam'))
print(f1('beef', eggs='spam'))
print('-'*20)
print(f2('beef'))
print(f2('beef', 'spam'))
print(f2('beef', eggs='spam'))
print(f1.__annotations__)


def f3(food: str, price: int, quantity: int) -> int:  # write a metadata of return type can be check use __annotations__
    print(food, 'total cost:', str(price*quantity))
    return price*quantity


f3('apple', 2, 10)
print(f3.__annotations__)
