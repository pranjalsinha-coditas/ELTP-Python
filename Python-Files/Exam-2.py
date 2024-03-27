data_types_set_1 = {"List", "Set", "Dictionary", "Bytearray", "Array"}

mutable_Data_Types = {f"Data-Type-{i+1}": data_type for i, data_type in enumerate(data_types_set_1)}

print(mutable_Data_Types)

# {'Data-Type-1': 'Set', 'Data-Type-2': 'Bytearray', 'Data-Type-3': 'Array', 'Data-Type-4': 'Dictionary', 'Data-Type-5': 'List'}

data_types_set_2 = {"Integers", "Floating-point-number", "Boolean", "Strings", "Tuples", "Frozen-set", "Byte"}

immutable_Data_Types = {
    f"Data-Type-{i+1}": data_type for i, data_type in enumerate(data_types_set_2)
}

print(immutable_Data_Types)

# {'Data-Type-1': 'Tuples', 'Data-Type-2': 'Frozen-set', 'Data-Type-3': 'Floating-point-number', 'Data-Type-4': 'Strings', 'Data-Type-5': 'Integers', 'Data-Type-6': 'Byte', 'Data-Type-7': 'Boolean'}

# - Object Typesb / Data Types
# - Number : 1234, 3.1415, 3+4j, ob111, Decimal(), Fraction()
# - String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m', 
# - List: [1, [2, 'three'], 4.5], list(range(10))
# - Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
# - Dictionary : {'food' : 'spam', 'tatse' : 'yum'}, dict
# (hours=10)

#  -  Set : set('abc'), {'a', 'b', 'c'}
#  - File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')
#  - Boolean : True, False
#  - None : None
#  - Functions, modules, classes
# - Advance: Decorators, Generators, Iterators, Comprehensions, Context Managers

# x = 2
# y = 3
# z = 4

# x+y
# int(2.32)
# float(40)
# (x, y, z)
# x+1, y*2
# (y % 2)
# z ** 2
# result = 1/3.0
# repr('chai')
# str('chai')
# 1 < 2
# 5.0 == 5.0
# 4.0 != 5.0 
# x<y<z
# 999999999999999999 * 2.1
# import random 
# random.random()
# random.randint(15, 20)
# l1 = ['lemon', 'masala', 'ginger', 'mint']
# random.choice(l1)
# random.shuffle(l1)
# from decimal import Decimal 
# Decimal('0.1')
# from fractions import Fraction
# myFra = Fraction(2, 7)
# setone = {1, 2, 3, 4}
# setone & {1, 3}
# setone | {1, 3}
# type(True)

squared_num = {x:x**2 for x in range(6)}
keys = ["Masala", "Ginger", "Lemon"]
keys

default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

new_dict = dict.fromkeys(keys, keys)
print(new_dict)

tea_types = ("Block", "Green", "Oolong")
print(tea_types)

tea_types[0]
tea_types[-1]
tea_types[1:]
len(tea_types)

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if 'Green' in all_tea:
    print("I have green tea")
    
more_tea = ("Herbal", "Earl Grey", "Hrebal")
more_tea.count("Herbal")
more_tea.count("Herb")
print(tea_types)

(black, green, Oolong) = tea_types
black
type(tea_types)
("", (1, 2, 3), "")





