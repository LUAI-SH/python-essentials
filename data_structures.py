# Lists
from array import array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2])  # 3
print(numbers[1:4])  # [2,3,4]
print(numbers[:4])  # [1,2,3,4]

# List Unpacking
first, second, *other, last = numbers

# Looping over list
for number in numbers:
    pass
# with index
for index, number in enumerate(numbers):
    print(index, number)

# Lambda Function
products = [("Macbook", 2000), ("iPhone", 1000)]

products.sort(key=lambda product: product[1])
print(products)

# List Comprehensions
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Tuples
point_3d = (1, 2, 3)  # Immutable
# point_3d[0] = 8  # TypeError

# Swapping Variables
x1 = 10
y1 = 11

x1, y1 = y1, x1

# Arrays (for large lists > 10,000 items)
# type codes -> https://docs.python.org/3/library/array.html
numbers_arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8])

# Sets
numbers_set = set(numbers)  # {1,2,3,4,...}
other_set = {1, 5, 7}
print(numbers_set & other_set)  # intersection operation
print(numbers_set | other_set)  # union operation
print(numbers_set - other_set)  # difference operation
print(numbers_set ^ other_set)  # symmetric difference


# Dictionaries
point = {'x': 1, 'y': 2}
point['z'] = 3  # add
del point['x']  # delete

for k, v in point.items():
    print(k, v)

# Dictionaries Comprehensions
doubles = {x: x*x for x in numbers}
print(doubles)

# Generator Expressions


def get_number():
    for n in range(numbers):
        yield n


# Unpacking Operator
list_1 = [1,2]
lis_2 = [2,4]
combined = [*list_1, *lis_2] # [1,2,2,3]
combined_as_set = {*list_1, *lis_2} # [1,2,2,3]
letters = [*"hello"]
point_1 = {'x': 1, 'y': 2}
point_2 = {'x': 6, 'z': 3}
combined = {**point_1, **point_2} # {'x': 6, 'y': 2, 'z': 3}
