
UPPER_LIMIT_PRIME = 19

def is_prime(num):
 for n in range(1, num):
     if (num%n==0):
         return False
     return True

for i in range(1, UPPER_LIMIT_PRIME):
    print("Primes found:")
	if is_prime(i + 1):
			print(i + 1, end=" ")



