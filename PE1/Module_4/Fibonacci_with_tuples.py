


def my_factorial(num):
    if num < 1:
        return 1
    product = num * my_factorial(num - 1)
    return product

    
print(my_factorial(5))
