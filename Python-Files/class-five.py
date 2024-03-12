names = ([0, 'a'], (1, 'b'), (2, 'c'))
print(names)

# operations to be performed =>
names = names + ((4, 's'), )
print(names)

names = names[:2] + ((4, 'mid'), ) + names[3:]
print(names)

names = ((10, 's'), ) + names
print(names)

names = names[1:5]
print(names)

names = names[:4]
print(names)

names = names[:2] + ((4, 'mid'), ) + names[3:]
print(names)

names = names[1:]
print(names)

# destructuring with rest operators
# index method and count method for tuples 
# keep playing with tuples and indexing, slicing and its indexes
# using .___add___ methods or use '+' operator
# please keep adding tuples and all
# study the methods of tuples very nicely 
# study packing and unpacking 

# arr[start:stop]         # items start through stop-1
# arr[start:]             # items start through the rest of the array
# arr[:stop]              # items from the beginning through stop-1
# arr[:]                  # a copy of the whole array
# arr[start:stop:step]    # start through not past stop, by step

def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
fun(*my_list)

args = [0, 1, 4, 9]

range(3, 6)

args = [3, 6]

range(*args)

def mySum(*args):
    return sum(args)

print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

def fun1(a, b, c):
    print(a, b, c)

def fun2(*args):
    args = list(args)
    args[0] = 'GeeksForGeeks'
    args[1] = 'awesome'

    fun1(*args)

fun2('Hello', 'beautiful', 'world!')

def func(a, b, c):
    print(a, b, c)

d = {'a' : 2, 'b' : 3, 'c' : 4}
func(**d)

def fun(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))

fun(name = "geeks", ID = "101", language = "Python")

a, b, c = '123'  
print(a)  
print(b)  
print(c)  
print("Unpacking lists")  
a, b, c = [1, 2, 3]  
print(a)  
print(b)  
print(c)  
print("Unpacking generators")  
gen = (i ** 2 for i in range(3))  
a, b, c = gen  
print(a)  
print(b)  
print(c)  
print("Unpacking dictionaries (keys, values, and items")  
my_dict = {'one': 1, 'two':2, 'three': 3}  
a, b, c = my_dict  # Unpack keys  
print(a)  
print(b)  
print(c)  
print("Unpack values")  
a, b, c = my_dict.values()    
print(a)  
print(b)  
print(c)  
print("Unpacking key-value pairs")  
a, b, c = my_dict.items()    
print(a)  
print(b)  
print(c)  

gen = (2 ** x for x in range(15))  
print(gen)  
*g, = gen  
print(g)  
range = range(10)  
*r, = range  
print(r)  
