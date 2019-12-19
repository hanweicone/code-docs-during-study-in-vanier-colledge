from package1 import p1m1 # import module
from package1.p1m1 import p1m1func2 # import function in the module
from package1 import *
p1m1.p1m1func1()  # use function from imported module
p1m1func2()  # use function from imported function
# p1m2.p1m2func1() # in pakage1 __init__.py do not define __all__ include all modules
# import package1 # can not just import package,need to import module or function

from package2 import *  # in __init__py define __all__
p2m1.p2m1func1()
p2m2.p2m2func1()


