#Building Lists

# Task-1
evens_to_50 = {
    index for index in range(51) if index % 2 == 0
}
print(evens_to_50)

# Task-2
new_list = {
    index for index in range(1, 6)
}
print(new_list)

# Task-3
doubles = {
    index * 2 for index in range(51)
}
print(doubles)

# Task-4
doubles_by_3 = {
    index * 2 for index in range(51) if index * 2 % 3 == 0
}
print(doubles_by_3)

# Task-5
Pattern_c = {
    "C" for index in range(11)
}
print(Pattern_c)

# Task-6
cubes_by_four = {
    x ** 3 for x in range(1, 11) if x ** 3 % 4 == 0
}
print(cubes_by_four)

# Task-7
list = [index ** 2 for index in range(1, 11)]
print(list[2:9:2])

# Task-8
Odd_nums = [index for index in range(1, 11)]
print(Odd_nums[::2])

# Task-10
Alphabets = ['A', 'B', 'C', 'D']
print(Alphabets[::-1])

# Task-11
to_21 = [index for index in range(1, 22)]
print(to_21)

odds = [to_21[::-2]]
print(odds)

middle_third = {
    index for index in range(8, 15)
}
print(middle_third)

# Important anonymous functions
# lambda
my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "CSS", "Python", "Ruby"]
print(filter(lambda x: x == "Python", "JavaScript"))

squares = [x ** 2 for x in range(30, 71)]
print(filter(lambda x: x in x >= 30 and x <= 70, squares))

movies = {
    "Monty Python`s and the Holy Grail": "Great", 
    "Monty Python`s Life of Brian" : "Good", 
    "Monty Python`s Meaning of Life" : "Okay"
}
print(movies.items())

three_fives = [index for index in range(1, 16) if index % 3 == 0 or index % 5 == 0]
print(three_fives)

str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2

print(str[start:end:stride])

my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = (filter(lambda x: x != 'X', garbled))
print(message)
#output:
# I am another secret message!

