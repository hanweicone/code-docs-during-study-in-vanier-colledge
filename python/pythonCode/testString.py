import io
print("wsefwef")
a ="sdfkljsdlkfj"
print(a[1:5:2])

a = 3*'g'
print(a)
b = "sdfkj{1}jsdfjh{0}lkjsdf{name}"
b.format("0", "1", name="jim")
print(b)
print(b.format("0", "1", name="jim"))
c = b.format("0", "1", name="jim")
print(c)

str = "hello,sio"
str_sio = io.StringIO(str)
print(str_sio.getvalue())
str_sio.seek(1)
str_sio.write("h")
print(str_sio.getvalue())

str1 ='sdfdf'
print(id(str1))
print(id(str1.replace('s', '*', 1)))
