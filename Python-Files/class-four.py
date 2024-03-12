# ClassWork => 11th March, 2024

numbers = [1, 2, 3, 4, 5]

#make an array with different dictionaries having different arrays
Array = [
    {"name" : "Pranjal"}, 
    {"name" : "Shambhu"}, 
    {"name" : "Ravi"}
]

#delete the second dictionary
Array.pop(1)
print(Array)

#add the fourth dictionary with another name
Array.insert(4, {
    "name" : "Nitya"
})
print(Array)

People = [
    {"name" : "A"}, 
    {"name" : "B"}, 
    {"name" : "C"}, 
    {"name" : "D"}
]

People.remove({"name" : "A"})
print(People)

three_odd_numbers = [3, 5, 7, 9]
three_even_numbers = [2, 4, 6, 8]

merged_array = [*three_odd_numbers, *three_even_numbers]
print(merged_array)

print(three_odd_numbers.__len__())
print(len(three_odd_numbers))

List = ['Mathematics', 'Chemistry', 1997, 2000, 'Mathematics']
List.append(20544)
List.insert(2, 10087)
print(List)
print(len(List))

# min, max, sum, pop, del, remove, count
# Reverse flag is set for true while we use sort

# cloning or cppying list using 
# => slicing technique

import copy

original_numbers_list = [1, 2, 3, 4, 5]
cloned_slice_copy = original_numbers_list[:]

cloned_extend_copy = original_numbers_list.copy()
print(cloned_extend_copy)
print(cloned_slice_copy)

original_list = [1, 2, [3, 5], 4]
cloned_list_module = copy.copy(original_list)

cloned_list_append = []
for item in original_list:
    cloned_list_append.append(item)
    
print(cloned_list_append)

cloned_list_with_enumerate = original_list.copy()
print(cloned_list_with_enumerate)

cloned_list = copy.deepcopy(original_list)
print(cloned_list)

cloned_list_len = original_list[slice(len(original_numbers_list))]
print(cloned_list_len)
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

