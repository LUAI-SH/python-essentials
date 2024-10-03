# Variables
counter = 0
temperature = 3.8
is_deployed = True
name = "Leo"

# Formatted String
print(f"Counter value = {count}")

# Type Conversion

x = input("x: ")
y = int(x) + 1

int(x)
float(x)
str(x)
bool(0)  # False
bool("")  # False
bool(None)  # False
bool(0.0)  # False


# Comparison Operators
0 < 5  # True
1 >= '1'  # TypeError
"a" == "A"  # False

# Ternary Operator
age = 18
message = 'eligible' if age >= 18 else 'not eligible'


# Logical Operator 
visitor = False  
income = 50000  
has_good_credit = True
if (income >= 30000 or has_good_credit) and not visitor:
    pass

# Chaining Comparison Operator
if 18 <= age < 65:
    pass

# For Loop
for x in range(2):
    break

# While Loop
while x < 10: 
    break





