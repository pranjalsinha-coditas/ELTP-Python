#datatypes are just for showing in the code
prime_number: str = "abcd"
prime: int = "10"
prime_number = "11"
print(prime_number)
# output is 11

#int & float
integer: int  = 10
decimal: float = 12.5

print(type(integer))
# output is 10
print(type(decimal))
#output is 12.5

#string -> str
string_quotes = 'this is a string'
double_quotes = 'this is also a string'
null_line_string = """
this is a multiline
string
"""

print(type(string_quotes))
print(type(double_quotes))
print(type(null_line_string))

# booleans -> booleans
is_python: bool = True
is_javascript: bool = False
print(type(is_python))
print(type(is_javascript))

null_value = None #NEVER DO THIS
print(type(null_value))

#collection datatypes
#list[array], dictionary[object], tuples

numbers: list[int] = [1, 2, 3, 4, 5]
strings: list[str] = ["a", "b", "c"]
anything: list[any] = [1, 1.5, "a", False, None, [1, 2, 3]]

from typing import Any
anything: list[Any] = [1, 1.5, "a", False, None, [1, 2, 3]]

numbers_tuple: tuple[int] = (1, 2, 3, 4)
names_tuple = ("Aniruddha", ) #remember the comma
# names_tuple = ()

print(type(names_tuple))

#dictionary
#keys


