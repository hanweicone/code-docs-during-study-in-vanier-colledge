from . import testModule
from ..import p2m1  # ..means parent level of  relativeImport.py
# from ... import package1  # ...means parent parent level of relativeImport.py
from ...package1 import p1m1
def relative_func():
    testModule.test()
    p2m1.p2m1func1()
    p1m1.p1m1func1()
    # package1.p1m1.p1m1func1()

# relative_func() erro then run as __main__

# when in python console do like this:
# >>>from package2.testRelativeFrom.relativeImport import relative_func
# >>>relative_func()
# ValueError: attempted relative import beyond top-level package


'''
because package1 is under the project not under a package,
when use relative import to get packge1,
will cause beyond top-level package error

'''