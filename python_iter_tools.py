import time
# for line open('chai.py'):
#     print(line) # just use this in an integrated terminal
print("chai is here")
username = "hitesh"

# codes for the integrated terminal use python3 to run these

# f = open('/Users/coditas/Documents/GitHub/ELTP-Python/iter-tools')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line, end='')

# import time
# print("chai is here")
# username = "Pranjal"
# print(username)>>>

# test = "Pranjal"
# if not test:
#     print("chai")

# test = ""
# if not test:
#     print("chai")

# myList = [1, 2, 3, 4, 5]
# I = iter(myList)
# I
# I.__next__()
# I
# I.__next__()

# f = open('/Users/coditas/Documents/GitHub/ELTP-Python/iter-tools/python_iter_tools.py')
# iter(f) is f
# iter(f) is f.__iter__()

myNewList = [1, 2, 3]
iter(myNewList) is myNewList

D = {'a':1, 'b':2}
for key in D.keys():
    print(key)

I = iter(D)
print(I)
next(I)
next(I)
next(I)
next(I)

R = range(5)
P = iter(R)





