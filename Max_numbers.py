num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

maximum = max_between_two(num1, num2)
print(f"The maximum between {num1} and {num2} is: {maximum}")

Alternatively, you can use the built-in max() function:

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"The maximum between {num1} and {num2} is: {max(num1, num2)}")