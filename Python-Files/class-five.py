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

