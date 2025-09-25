What are Errors and Exceptions?

Error → Problem in the program that makes it stop running.

Exception → An error that occurs during program execution, but we can handle it so the program doesn’t crash.

Example:

print(10 / 0)   # ZeroDivisionError

 Exception Handling in Python

We use try – except blocks.

 Example 1: Handling Division by Zero
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")

 Example 2: Handling Multiple Errors
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter numbers only")

 Example 3: Using finally (runs always)
try:
    f = open("myfile.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program finished (with or without errors).")

 Example 4: Custom Exception with raise
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    else:
        print("You are eligible")

try:
    check_age(15)
except ValueError as e:
    print("Error:", e)


 Output:

Error: Age must be at least 18


⚡ So in short:

try → put risky code

except → handle the error

finally → always run cleanup code

raise → throw your own exception