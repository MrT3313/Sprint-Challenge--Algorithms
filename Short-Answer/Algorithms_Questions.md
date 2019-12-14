# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

a)
```python
    a = 0                     # O(1)      | # O(1)  | # O(n)
    while (a < n * n * n):    # O(n)      | # O(n)  
      a = a + n * n             # O(1)    |   # ^^
```
Answer: O(n)


b)
```python
  sum = 0             # O(1)         |   # O(1)        |   # O(1)          |  # O(n log(n))  
  for i in range(n):  # O(n)         |     # O(n)      |    # O(n log(n))  | 
    j = 1               # O(1)       |      ^^         |      ^^
    while j < n:        # O(log(n))  |    # O(log n)   |
      j *= 2              # O(1)     |      ^^         |
      sum += 1            # O(1)     |      ^^         |
```
Answer: O(n log(n))

c)
```python
  def bunnyEars(bunnies):

    # BASE CASE     
    if bunnies == 0:  # O(1)
      return 0          

    # RECURSION
    return 2 + bunnyEars(bunnies-1) # O(n)
```
Answer: O(n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

