# Cypher Shift.
source = input("Enter text to encyrpt, please: ")
cypher_shift = 0
while (cypher_shift < 1 or cypher_shift > 25):
    cypher_shift = int(input('Enter an integer shift value between 1 and 25 inclusive: '))

target=''
FIRST_LOWER = ord('a')
FIRST_UPPER = ord('A')
print("FIRST_LOWER: ", FIRST_LOWER)
print("FIRST_UPPER: ", FIRST_UPPER)

for ch in source:
    print("source: ", ord(ch))
    if not ch.isalpha():
        target += ch
        continue
    
    encoded_ord = ord(ch) + cypher_shift
    print("encoded_ord: ",encoded_ord)
    
    if str(ch).isupper() and encoded_ord > ord('Z'):
        encoded_ord = FIRST_UPPER + encoded_ord - ord('Z')-1
    elif str(ch).islower() and encoded_ord > ord('z'):
        encoded_ord = FIRST_LOWER + encoded_ord - ord('z')-1
    target += chr(encoded_ord)
    
print("Encoded text:", target)
