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

(a, b, c, d, e, f) = (1, 2, 3, 4, 5, 6)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

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
gen = (i**2 for i in range(3))
a, b, c = gen
print(a)
print(b)
print(c)

print("Unpacking dictionaries (key, valuesm and items: ")
my_dict = {'one' : 1, 'two' : 2, 'three' : 3}
a, b, c = my_dict
print(a)
print(b)
print(c)
print("Unpack values")
a, b, c = my_dict.values()
print(a)
print(b)
print(c)

[a, b, c] = 1, 2, 3
print(a)
print(b)
print(c)

[a, b, c] = {'x', 'y', 'z'}
print(a)
print(b)
print(c)

*a,  = ('x', 'y', 'z')
print(a)

a, b, *c = 1, 2, 'x', 'y', 'z'
print(a)
print(b)
print(c)

*a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

*a, b, c, d = 1, 2, 3
print(a)
print(b)
print(c)
print(d)

gen = (2**x for x in range(15))
print(gen)
*g, = gen
print(g)
range = range(10)
*r, = range
print(r)

emp = ["Mathew Wade", "400000$", "Software Engineer"]
name = emp[0]
age = emp[1]
profile = emp[2]
print("The name is: ", name)
print("The age is: ", age)
print("the profile is:", profile)

def powers(number):
    return number, number ** 2, number ** 3

result = powers(8)
print(result)
number, square, cube = powers(8)
print(number)
print(square)
print(cube)

*_,cube = powers(2)
print(cube)

tup = (1, 2, 3)
print((0, *tup, 4))
list1 = [1, 2, 3]
print([0, *list1, 4])
my_set = {1, 2, 3}
print({0, *my_set, 4})
print([*my_set, *list1])
my_str = "123"
print([*my_set, *list1, *tup, *my_str])

numbers = {"one" : 1, "two" : 2, "three" : 3}
letters = {"a" : "Apple", "b" : "Bat", "c" : "Cat"}
combine = {**numbers, **letters}
print(combine)


