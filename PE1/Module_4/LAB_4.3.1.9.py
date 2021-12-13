
UPPER_LIMIT_PRIME = 21

def is_prime(num):
    for i in range(2, num):
        rem = num%i
        if (rem==0):
         return False
    return True

for i in range(2, UPPER_LIMIT_PRIME):
   
    if is_prime(i):
        print(i, end=" ")



