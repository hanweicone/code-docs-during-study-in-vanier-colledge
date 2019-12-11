import unittest
loader = unittest.TestLoader()
#test file name must start with 'test'

start_dir = "C:/PycharmProjects/testUnit/test"
# suite = loader.discover(start_dir)  # just discover test*.py,use pattern "*.py" to find all
suite = loader.discover(start_dir, pattern="*.py")
runner = unittest.TextTestRunner()
runner.run(suite)

 # run code in teminal use python.exe install in computer
 
 # C:\Python\Python38-32\python.exe -m unittest discover "C:\PycharmProjects\testUnit\test" -v
 
 # run code in terminal use python.exe in the project,notice that runMultiTestFile.py is in the project root with venv directory,venv\Scripts has python.exe
 
 # venv\Scripts\python.exe -m unittest discover "C:\PycharmProjects\testUnit\test" -v
#import sys

#print(sys.path)

# notice that sys.path already has venv and also Python38-32 so we can use the short cut path of python.exe
# python.exe -m unittest discover "C:\PycharmProjects\testUnit\test" -v
#notec that do not name py files start with numbers,it will not discover if file name start with numbers
'''
-p, --pattern pattern
Pattern to match test files (test*.py default)
if file name not start with test,we can use pattern
see https://docs.python.org/3/library/unittest.html
'''
# python -m unittest discover -s C:\PycharmProjects\testUnit\test -p "*.py" -v
