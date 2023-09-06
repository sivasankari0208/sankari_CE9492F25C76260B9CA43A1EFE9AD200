def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

number = int(input("enter a number:"))

if number < 0:
  print("Factorial is not defined for negative numbers.")
elif number == 0:
  print("The factorial 0f 0 is 1")
else:
  result = factorial(number)
  print(f"the factorial of {number} is {result} ")
  