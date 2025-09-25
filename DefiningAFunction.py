What is a function?

A function is a block of code that runs only when you call it.

It helps reuse code.

It can take inputs (called parameters).

It can return outputs.

 1. Defining and Calling a Function
def greet():
    print("Hello! Welcome to Python.")

# call the function
greet()


 Output:

Hello! Welcome to Python.

 2. Function with Parameters
def add(a, b):
    print("Sum =", a + b)

add(5, 3)
add(10, 20)


 Output:

Sum = 8
Sum = 30

 3. Function with Return Value
def square(x):
    return x * x

result = square(6)
print("Square =", result)


 Output:

Square = 36

 4. Function with Default Parameter
def greet(name="Guest"):
    print("Hello", name)

greet("Alice")
greet()


Output:

Hello Alice
Hello Guest

 5. Function with Loop Inside
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)


Output:

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50