
# FizzBuzz
def fizzbuzz(n=15):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
# Prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]
# Factorial
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Fibonacci
def fibonacci(n=10):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
#Reverse string
def reverse_string(text):
    return text[::-1]
# Sum of digits
def sum_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Largest number using *args
def largest(*args):
    if not args:
        return None
    biggest = args[0]
    for number in args:
        if number > biggest:
            biggest = number
    return biggest

print("FizzBuzz")
fizzbuzz()

print("Prime:", is_prime(17))
print("Palindrome:", is_palindrome("madam"))
print("Factorial:", factorial(5))
print("Fibonacci:")
fibonacci()
print("Reverse:", reverse_string("Python"))
print("Digit sum:", sum_digits(1234))
print("Largest:", largest(10, 25, 7, 40))

# Default arguments,kwargs
def show_details(name="Sobika", **kwargs):
    print("Name:", name)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_details(language="Python", day=1)
