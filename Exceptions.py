# Try - except - else
try:
    input_number = int(input('number: '))
    print(input_number / 0)
except ValueError:
    print('Value error.')
except ZeroDivisionError:
    print('Zero division error.')
else:
    print('No Exceptions occurs.')
finally:  # Clean Up
    print('This will be always executed.')


# Raising Exceptions
# list: https://www.w3schools.com/python/python_ref_exceptions.asp
def calculate_tax(income):
    if income < 0:
        raise ValueError("Income cannot be negative value.")
    
try:
    calculate_tax(-4)
except ValueError as error:
    print(error)