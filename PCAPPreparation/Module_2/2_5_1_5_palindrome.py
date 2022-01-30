''' Lab 2.5.1.5 Palindrome '''
source = input("Input a string to check if it is a palindrome: ")

stripped = source.lower().replace(" ", '')

is_a_palidrome = True
length = len(stripped)
if (length <2):
    print("It's not a palindrome")

for i in range(0, (length)//2):
    back_end = -(i+1)
    is_a_palidrome = is_a_palidrome and (stripped[i] == stripped[back_end])
    if not is_a_palidrome:
        break
    
print("Is it a palindrome?:", is_a_palidrome)
        
    
