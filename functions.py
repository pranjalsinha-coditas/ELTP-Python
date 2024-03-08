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

 