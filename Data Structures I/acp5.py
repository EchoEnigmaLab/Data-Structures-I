# Take two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Start checking from the larger number
if num1 > num2:
    lcm = num1
else:
    lcm = num2

# Keep checking until we find a common multiple
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break

    lcm = lcm + 1

print("LCM :", lcm)