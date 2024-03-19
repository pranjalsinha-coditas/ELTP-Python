# most important please keep revising javascript day by day
# Just the list of main topics 

def add(a: int, b: int) -> int:
    return a+b

def subtract(x: int, y: int) -> int:
    return x-y

addition = add(3, 4)
subtraction = subtract(3, 4)

#missing positional arguments : ERROR for add()

def multiply(n1: int, n2: int) -> int:
    """
    @param: n1 int
    @param: n2 int

    returns n2 int
    """
    return n1 * n2

add # reference to the fn expression
add(2, 5) # => executes code at reference

add_fn = add

print(add_fn(5, 6))

#lambda func

from typing import Callable

divide: Callable[[int, int], int] = lambda n1 , n2: n1 / n2 
divide.__doc__ = """param: n1 int, param: n2 int"""
#see how callable works for displaying the datatype of this lambda func
#putting doctstring for a lambda
print(divide(5, 6))

# find method in python for arrays

from typing import TypeVar

#Generics
T = TypeVar('T')

def find(array: list[T], elem: T) -> T | None:
    for item in array:
        if elem == item:
            return elem.indexOf()
        else:
            return False



one = find([1, 2, 3, 4], 10)
print(one)

# recreation of loadfactory example in python 
# carloan = 8, homeloan = 10, personal_loan = 12


def loanfactory(principal: int, loan: str, time: int) -> int:
    if loan == "Car Loan":
        """For Car Loan"""
        interest = (principal * 8 * time) / 100
        amount = interest + principal
        return amount
    elif loan == "Home Loan":
        """For Home Loan"""
        interest = (principal * 10 * time) / 100
        amount = interest + principal
        return amount
    elif loan == "Personal Loan":
        """For Personal Loan"""
        interest = (principal * 12 * time) / 100
        amount = interest + principal
        return amount
    else:
        return 0

# #Example 
my_amount=loanfactory(10000, "Car Loan", 4)
print(my_amount)

# -> Correct Solution

def loan_factory(rate_of_interest):
    def calculator(p, n):
        return p * n * rate_of_interest / 100
    
    def update_calculate(updateRate):
        nonlocal rate_of_interest
        if updateRate is not None:
            rate_of_interest = updateRate
        
    return [calculator, update_calculate]
    

# we have to use just one global or nonlocal roi(variable being used)
# redo all of these again scoping, closure 

rate_of_interest, updateRate = loan_factory(11)
print(loan_factory(11))









                               


    


