# name = {"name":"shreya", "age":32, "department":"ase"}
# for key in name:
#     print(name[key])

# #iterators
# person = ["shreya", "an", "is"]
# my_iterator = iter(person)
# print(my_iterator.__iter__)
# print(list(my_iterator))
# print(my_iterator.__next__)
# print(next(my_iterator))
# print(iter(my_iterator))
# print(my_iterator)

# for i in my_iterator:
#     print(i)


#Take infinite loops
# without iterables nothing can become interator
# without iterable i we cannot iterate
# build a variable with next that uses while loop to iterate over person    
# while i<len(person):
#     print(next(my_iterator))
# Q.1 function that returns a next prime number without using any kind of generator or my_iterator
def get_next_prime(num):
    def is_prime(numreq):
        if numreq <= 1:
            return False
        for i in range(2, int(numreq**0.5) + 1):
            if numreq % i == 0:
                return False
        return True
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1
initial_value = 11
result = get_next_prime(initial_value)
print(result)

