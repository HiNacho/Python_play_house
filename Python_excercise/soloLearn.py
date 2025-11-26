# Question 1
import doctest

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
# print(func(7))


# Day 2
# Question 1
class Foo:
    def bar(self):
        pass
# print(Foo.bar.__name__)

# __name__ is an attribute that returns the name of function as a string
def hello():
    pass
# print(hello.__name__)


class Foo:
    def bar(self):
        print(self)
# print(Foo.bar) # function is attached to an instance
# print(Foo().bar) # raw function not bound to any specific instance (object)

# Analogy
"""
class = blueprint
object/instance = actual house built using the blueprint
methods = instructions on how the house is to be built
"""

# Question 2
from functools import reduce
arr = [1,2,3,4,3,2,1]
# a = list(map(lambda x:x%2 == 0, arr))
# a = list(filter(lambda i: i%2==0,arr))
a = reduce(lambda i,j: i + j, arr)
# print(a)

"""
map() does not reduce or filter
"""

# Question 3
# appropriate use of reverse()
list1 = [1,2,3,4]

# correct application
# list.reverse()

# not correct use
# list = reverse(list)

# reversed() does not return a list, it returns an iterator
# print(list(reversed(list1)))

# print('java' > 'javascript')

class Animal:
    def __init__(self, id):
        self.id = id
crow = Animal(100)
crow.__dict__["age"] = 49

# print(crow.age + len(crow.__dict__))



"""
initially crow.__dict__ contains {"id":100}
this adds {"id" : 100, "age": 49}
"""

# Question 4
n = 0
a = 5
b = 3

while a > 0:
    a -= 1
    n += 1

# print(n)

# Question 5
a = [1,2,3]
b = iter(a)

# print(b.__next__(),"")
# print(next(b),"")
# print(next(b),"")
# print(b.__next__(),"")


# Question 6
a = [[]] * 2
# print(a)
a.append(2)
# print(a)
# Question 7

a = 1 == 1 or 1 != 1
b = a==1 and 2 != 2.0

if b:
    print(b)
else:
    print(a)

# Question 8
x = 2
a = [x ** 3-1 for xi in range(7)]
# print(a)

# Question 9
a = dict.fromkeys(range(5), 1)
y = list(a.values()).count(2)
# print(y)

"""
range = 1-5
dict.fromkeys {0:1,1:1,2:1,3:1,4:1}
a.values() [1,1,1,1,1]
count(2) how many times 2 appears which is 0
"""

# Question 9
mySet = set([1,"1",int(1.0),4//3,4/3])
# print(len(mySet))

# Day 3
# Question 10
class sololearn():
    pass
if __name__ == "__main__":

    x = sololearn()
    y = sololearn()
    if(x == y):
        print(1)
    else:
        print(2)

# Question 11
# what is the output of the following code?
# print(type(lambda:None))
# a lambda in python is just a shortcut in creating a function

# Question 12
__orangenum = 5
# any attribute that begins with double underscores (__) and does not end with them are declared as strongly private

# Question 13
x = {1:0,0:1}
y = [1,[4,6,5,4],2]

print(list(set(y[x[0]]))[1])

# yield turns a function to a generator

# Question 14
lst = [1,2,3,4,5]
for i in range(1,6):
    lst[i:i] = [i]
print(lst)

# Question 15
A = 1
B = A
idA = id(A)
idB = id(B)

A = 2
idA2 = id(A)
print(idA == idB)
print(idA == idA2)

# since A and B have the exact same value 1 as an integer, it is True

# Question 16
def Foo(n):
    def multiplier(x):
        return x * n
    return multiplier

a = Foo(4)
b = Foo(4)

# print(a(b(5)))

# Question 17
a = [0,1,2,3]
a[:] = [sum(a)]
# print(len(a))

# Question 18
k = list(map(
    lambda x,y : x + y,
    list(range(100)),
    list(range(12))
))

# print(len(k))

# Question 19
# is the below comparison True?
print([4,0]*4 == -4 * [0,4])
# list cannot be multiplied with a negative integer

# Question 20
a = (0)
b = [0],[[0]], {0}, [(0)]
#for i in b:
#    print(a in i)

# Question 21
import re
first = re.match("(car)?","racecar")
second = 0**0
if second and first:
    print("x")
elif second or first:
    print("y")
else:
    print("z")

class A:
    a = print(5)
    def get_a(self):
        return(self.a)
a = A()
#vprint(a.get_a())

# Question 22
a = [1,2]
b = [3,2]
c = [[i*j for i in a ] for j in b]
print(c[1][1])