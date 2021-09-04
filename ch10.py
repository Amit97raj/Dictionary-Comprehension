 # Python Basics Chapter 10:
# =========================

# 1. Dictionary Comprehension

# Create a dictionary of squares from 1 to 3 -
# Output : squares = {1: 1, 2: 4, 3:9}

# squares = {num : num**2 for num in range(1, 10)}
# print(squares)

# squares = {f"Square of {num}" : num**2 for num in range(1, 10)}
# print(squares)

# Create a dictionary of characters counts from string.

# name = "Anshul"
# chars_count = {ch : name.count(ch) for ch in name} 
# print(chars_count)

# 2. Dictionary Comprehension With If Else 

# Create a dictionary of odd evens -
# Output : odd_even = {1: 'odd', 2: 'even', 3: 'odd'}

# odd_even = {i : 'even' if i % 2 == 0  else 'odd' for i in range(1, 4)}
# print(odd_even)

# odd_even = {i : ('even' if i % 2 == 0  else 'odd') for i in range(1, 4)}
# print(odd_even)

# even = {i : i**2 for i in range(1, 4) if i % 2 == 0}
# print(even)

# 3. Sets Comprehension

# Create a set of squares from 1 to 10 -

# squares = {i**2 for i in range(1, 11)}
# print(squares)

 names = ['Anshul', 'Manya', 'Neha', 'Nidhi']

 first_chars = {name[0] for name in names}
 print(first_chars)
