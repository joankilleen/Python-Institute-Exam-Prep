def exponent(y):
    def power(x):
        return x ** y
    return power

my_power = exponent(10)
square = exponent(2)
cube = exponent(3)

def supply_x(x):
    def unnamed_fn(func):
        return func(x)
    return unnamed_fn

even = lambda x: True if x%2==0 else False

test_five = supply_x(5)

isEven = test_five(even)

print(isEven)