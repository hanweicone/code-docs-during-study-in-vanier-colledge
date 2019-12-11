import re
import time
print('Hello Python')
a = ['sdf','wee','wefwf']
print('*'.join(a))
py = 'U,like,me like python'
print("python" in py)#in /not in check substring
# print(py.split(',',' ')) #not work
print(re.split(',| ',py))#split use re,and with delimiters ',' and ' '

time01 = time.time()
a = ''
for x in range(2000000):
    a += 'hello'#use + every time creat a new object,spend lots of time

time02 = time.time()

print("spend time use '+' :"+str(time02-time01))

time03 = time.time()
li =[]
for x in range(2000000):
    li.append("hello")#append string in list than use join,just have one object,save time
a = "".join(li)
time04 = time.time()

print('spend time use join:'+str(time04-time03))
