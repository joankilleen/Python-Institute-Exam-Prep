OFF = ' '
ON = '#'
SEP="  "
ROW_COUNT = 5

ZERO = [ON+ON+ON, ON+OFF+ON, ON+OFF+ON, ON+OFF+ON, ON+ON+ON]

ONE = [OFF+ON+OFF, OFF+ON+OFF, OFF+ON+OFF, OFF+ON+OFF, OFF+ON+OFF]

TWO = [ON+ON+ON, OFF+OFF+ON, ON+ON+ON, ON+OFF+OFF, ON+ON+ON]

THREE = [ON+ON+ON, OFF+OFF+ON, ON+ON+ON, OFF+OFF+ON, ON+ON+ON]

FOUR = [ON+OFF+ON, ON+OFF+ON, ON+ON+ON, OFF+OFF+ON, OFF+OFF+ON]

FIVE = [ON+ON+ON, ON+OFF+OFF, ON+ON+ON, OFF+OFF+ON, ON+ON+ON]

SIX = [ON+ON+ON, ON+OFF+OFF, ON+ON+ON, ON+OFF+ON, ON+ON+ON]

SEVEN = [ON+ON+ON, OFF+OFF+ON, OFF+OFF+ON, OFF+OFF+ON, OFF+OFF+ON]

EIGHT = [ON+ON+ON, ON+OFF+ON, ON+ON+ON, ON+OFF+ON, ON+ON+ON]

NINE = [ON+ON+ON, ON+OFF+ON, ON+ON+ON, OFF+OFF+ON,  OFF+OFF+ON]

display_dict = {'0': ZERO, '1': ONE, '2': TWO, '3': THREE, '4': FOUR, '5': FIVE, '6': SIX, '7': SEVEN, '8': EIGHT, '9': NINE}
numbers_array = []

def display_number(numbers_array):
    j=0
    for j in range(5):
        row_str = ""
        for n in numbers_array:
            row_str = row_str + n[j] + SEP
        print(row_str)

while True:
    number_str = input("Enter the number to be displayed (positive integer): ")
    try:
        val = int(number_str)
        if val < 0:
            print("That is not a positive integer!")
            continue
        break
    except ValueError:
        print("That's not an int!")
        
for char in number_str:
    numbers_array.append(display_dict[char])
    
display_number(numbers_array)


