# Question 1

# this is correct. the "".join() method accepts a group of strings and glue them together
#print("".join(['h','i']))

# this is correct because there are two slots {} {} and the * operator unpacks the list to provide two items
# print("{}{}".format(*['h','i']))

# this will return an index error because it has two slots {} {} but only one arguement is available
# print("{}{}".format(['h','i']))

# this is not correct as "".join accepts one argument but the * unpacks the list, providing 2 arguments
# print("".join(*['h','i']))

# Question 2
a = [1,5,6]
# this copies the content in variable a
b = a[::]
# this outputs True
# print(a == b)

# this outputs False
# print(a is b)

b[2] = 2

# when copying, the original code is not affected
# print(a)
# print(b)

# Question 3
def f(m:str, v:str) -> int:
    return f.__annotations__
# print(f("a","b")["m"])

# Question 4
a = 0
b = 0
x = [a,b]
y = (1,2)
x = y
# print(x,a,b)
# it will output (1,2) 0 0

# Question 5
# this code demonstrates how eval() works. eval() takes a string and execute it as if it were a code
def func(n):
    y = "*".join(str(x) for x in range (1,n,2))
    return eval(y)
print(func(7))