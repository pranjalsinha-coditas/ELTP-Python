number = str(5)
print(number)
# output 5
x = 5

number: int
print(number)
# output 5
number = 10

# x + ignored => no KeyError
# print(x)
# print(number) => error

# no camel casing only underscores in python
teacher_name = "Lady"
print(teacher_name)
# output is Lady

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







