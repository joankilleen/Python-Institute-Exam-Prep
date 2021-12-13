x = float(input("Enter value for x: "))
if (x==0):
    print("Cannot divide by 0!")
    exit()
    
def get_divider(q):  
    return float(q + (1/q))


# Write your code here.
y=float(1/(x + (1/(x + 1/(x + 1/x)))))

z=1/x
for n in range(3):
    z=1/(x+z)

print("y=", y)
print("z=", z)
