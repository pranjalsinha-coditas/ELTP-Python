def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %f" %(bill))
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.5
    print("With tip: %f" %(bill))
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

def power(base, exponent):
    result = base ** exponent
    print("%d to the powert of %d is %d." %(base, exponent, result))

print(power(37, 4))

def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

print(one_good_turn(2))
print(deserves_another(2))

def cube(num):
    return num ** 3;

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

import math
print(math.sqrt(25))

from math import sqrt 
print(math.sqrt(12789))

import math 
everything = dir(math)
print(everything)

def biggest_number(*args):
    print(max(args))
    return max(args)

def smallest_number(*args):
    print(min(args))
    return min(args)

def distance_from_zero(arg):
    print(abs(arg))
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

n = [ 1, 2, 3, 4, 5]
print(n.pop(1))
print(n.remove(1))
del(n[1])

def list_extender(lst):
    lst.append(9)
    return lst
print(list_extender(n))

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))

# methods for traversing in list:
# for item in list:
#     print(item)

# for i in range(len(list)):
#     print(list[i])

n = [3, 5, 7]
def total(number):
    result = 0
    for num in number:
        result += num
    return result

n = ["Miachel", "Lieberman"]

def join_strings(words):
    result = ""
    for word in words:
        result += word
    return result

print(join_strings(n))

list_of_lists = [[1, 2, 3], [4, 5, 6]]
for lst in list_of_lists:
    for item in lst:
        print(item)

