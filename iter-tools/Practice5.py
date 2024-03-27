def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(0.5 ** n) + 1))
print(is_prime(2))

def is_palindrome(s):
    return s == s[::-1]

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def count_characters(s, char):
    return s.count(char)

def sort_numbers(numbers):
    return sorted(numbers)

def get_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

def sum_of_digits(n):
    return sum(map(int, str(n)))

import copy

original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(original_list)

shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0][0] = 100
print(original_list)

deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[0][0] = 100
print(original_list)



