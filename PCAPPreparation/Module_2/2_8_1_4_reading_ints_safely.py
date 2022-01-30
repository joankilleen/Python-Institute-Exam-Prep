def read_int(prompt, min, max):
    value = None
    while True:
        try:
            value = int(input(prompt))
            assert value >= min and value <= max
            return value
        except ValueError:
            print("Not a vald integer. Try again")
        except AssertionError:
            print("Error: the value is not within permitted range(min..max)", min, max)
        continue


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
