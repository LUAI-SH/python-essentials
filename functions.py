# Declaration
def say_hello():
    print("Hi")

# Pass Argument


def increment(x, by=1):
    print(x+by)

# *args


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

# **args (kwargs)


def add_user(**user):
    print(user['name'])


add_user(id=1, name="Leo")
