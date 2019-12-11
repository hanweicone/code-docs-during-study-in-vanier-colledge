a, b = 0, 1
while a < 1000:
    print(a, end=' ')
    a, b = b, a+b
print('')
print('------')
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w),sep=' length : ')
for w in words:
    print(w+str(len(w)))