
def hi(name="yasoob"):
    return "hi " + name

print(hi())
# output: 'hi yasoob'
print(id(hi))
# We can even assign a function to a variable like
greet = hi
# We are not using parentheses here because we are not calling the function hi
# instead we are just putting it into the greet variable. Let's try to run this

print(greet())
# output: 'hi yasoob'

# Let's see what happens if we delete the old hi function!
#del hi
#print(hi())
#outputs: NameError

print(greet())
#outputs: 'hi yasoob'
print(id(greet))
#we can see:id(greet)==id(hi)