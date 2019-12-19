'''
In programming languages, a closure, also lexical closure or function closure,
 is a technique for implementing lexically scoped name binding in a language
 with first-class functions. Operationally, a closure is a record storing a
 function[a] together with an environment.[1] The environment is a mapping
  associating each free variable of the function (variables that are used locally,
   but defined in an enclosing scope) with the value or reference to which the name
    was bound when the closure was created.[b] Unlike a plain function,
    a closure allows the function to access those captured variables through
    the closure's copies of their values or references,
    even when the function is invoked outside their scope.

'''

def func1():
    str = 'hello'

    def innerfunc():
        print(str)
    return innerfunc


closure = func1()  # func1() return a function ,not the return of that function(no need to execute function)
closure()  # this is a closure example


def func2():
    str = 'hello'


    def innerfunc():
        print(str)
    return innerfunc()


closure = func2()  # func2() does not return anything,asign it to closure is not good
closure  # output 'hello'