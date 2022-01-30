birthdate_str = ""
while True:
    while len(birthdate_str) != 8 and not birthdate_str.isdigit():
        birthdate_str = input("Enter your birth date as digits in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY: ")
    
    sum = 0
    for i in range(8):
        sum += int(birthdate_str[i])
    
    print("Sum of birthdate: ", sum)
    digit_of_life = 0
    for digit in str(sum):
        digit_of_life += int(digit)
    print("Your digit of life is: ", digit_of_life)
    birthdate_str = ""
