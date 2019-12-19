import re
f = open('input.txt', 'r')
str1 = f.read()
str_list = re.split(';|\\\|,| |\*|\n|\'|"|\t|:|\.', str1)
# in python 3,all the string is unicode,in python 2 string is not unicode,
# isnumeric() method only works for unicode string.we need to cast x to unicode here
# dupe_index = {x: str_list.count(x) for x in str_list if not unicode(x, 'utf-8').isnumeric() and x != ''}  # for python2
# dupe_index = {x: str_list.count(x) for x in str_list if not x.digit() and x != ''}  # for python2
dupe_index = {x: str_list.count(x) for x in str_list if not x.isnumeric() and x != ''}  # for python3
f.close()
f = open('output.txt', 'w')
for k, v in dupe_index.items():
    f.write(k+' : '+str(v)+'\n')
f.close()

