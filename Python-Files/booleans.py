# a = True
# type(a)
# print(type(a))
# b = False
# type(b)
# print(type(b))

# x = 5
# y = 10
# print(bool(x==y))

# x = None
# print(bool(x))

# x = ()
# print(bool(x))

# x = {}
# print(bool(x))

# x = 0.0
# print(bool(x))

#Falsy Values
Empty_Lists = []
print(type(Empty_Lists))
Empty_Tuples = ()
print(type(Empty_Tuples))
Empty_Dictionaries = {}
print(type(Empty_Dictionaries))
Empty_sets = set()
print(type(Empty_sets))
Empty_String = ""
print(type(Empty_String))
Empty_ranges = range(0)
print(type(Empty_ranges))
Empty_Integer = 0
print(type(Empty_Integer))
Float = 0.0
print(type(Float))
Complex = 0j
print(type(Complex))
None
print(type(None))
False
print(type(False))


# Falsy values include empty sequences (lists, tuples, strings, dictionaries, sets), zero in every numeric type, None, and False.
# Truthy values include non-empty sequences, numbers (except 0 in every numeric type), and basically every value that is not falsy.
# They can be used to make your code more concise.

if(5<3):
    print("True")
else:
    print("False")

a = int(input("Please enter a number: "))

if(a > 0):
    print("a is a number")
else:
    print("Falsy, it must be zero")

#construct a definition for truthy and falsy values
    
print(bool(5))
print(bool(0))
print(bool([]))
print(bool({5, 5}))
print(bool(-5))
print(bool(0.0))
print(bool(None))
print(bool(1))
print(bool(range(0)))
print(bool(set()))
print(bool({5, 6, 2, 5}))

# def print_even_long(data):
#     if data:
#         for value in data:
#             if value % 2 == 0:
#                 print(value)
#     else:
#         print("The argument cannot be empty")
# my_number = print_even_long(16)
# print(my_number)

# def print_even(data):
#     if not data:
#         raise ValueError("The argument data cannot be empty")
#     for value in data:
#         if value % 2 == 0:
#             print(value)
# my_second_number = print_even(16)
# print(my_second_number)

class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def __bool__(self):
        return self.balance > 0

account1 = Account(500)
print(account1)

account2 = Account(400)
print(account2)
