# ELTP-Python

### 1. Write a program to find the factorial of a number.

``` bash
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        return True
def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

primes = prime_generator()
for _ in range(10):
    print(next(primes))

```

### 2. Write a program to find the factorial of a number.

``` bash
def is_factorial(num):
    if num == 0:
        return 1
    else:
        return num * is_factorial(num-1)

my_num = 4
print(is_factorial(my_num))

```

### 3. Implement a function to check if a string is a palindrome.

``` bash 
def is_palindrome(s):
    return s == s[::-1]
    
my_name = "radar"
print(is_palindrome(my_name))

```

### 4. Write a program to find the largest element in an array.

``` bash 
import math
def largest_element(num):
    return max(num)

my_num = [1, 2, 3, 4]
print(largest_element(my_num))
 
```

### 5. Implement a function to reverse a linked list.

``` bash
def reverse(self):
    prev, current = None, self.head
    while current:
        current.next, prev, current = prev, current, current.next
    self.head = prev
    
```


### 6. Write a program to sort an array of integers using the bubble sort algorithm.

### 7. Implement a function to calculate the Fibonacci sequence up to a given number.

### 8. Write a program to check if two strings are anagrams of each other.

### 9. Implement a function to find the shortest path in a graph using Dijkstra's algorithm.

### 10. Write a program to detect a cycle in a linked list.

### 11. Implement a function to find the median of two sorted arrays.

### 12. Write a program to calculate the sum of all prime numbers up to a given number.

### 13. Implement a function to convert a binary tree to its mirror image.

### 14. Write a program to find all permutations of a given string.

### 15. Implement a function to check if a binary tree is balanced.

### 16. Write a program to find the longest common subsequence of two strings.

### 17. Implement a function to perform binary search on a sorted array.

### 18. Write a program to generate all possible combinations of a given list of numbers.

### 19. Implement a function to perform matrix multiplication.

### 20. Write a program to find the intersection of two arrays.

### 21. Implement a function to reverse a stack using recursion.

### 22. Write a program to check if a number is a power of two.

### 23. Implement a function to find the missing number in an array of integers.

### 24. Write a program to convert a decimal number to binary.

### 24. Implement a function to perform depth-first search (DFS) on a graph.

### 25. Write a program to find the longest increasing subsequence of an array.

### 24. Implement a function to detect if a linked list has a loop.

### 25. Write a program to implement a priority queue.

### 26. Implement a function to calculate the edit distance between two strings.

### 27. Write a program to find the maximum sum subarray of a given array.

### 28. Implement a function to find the kth largest element in an array.

### 29. Write a program to find the maximum sum subarray of a given array.

### 30. Implement a function to find the kth largest element in an array.
