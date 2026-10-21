#var 
age = 20
phno = 123456789
name = "sobika"
print("age:", age)
print("phno:",phno)
print("name:", name)

# numbers
a = 10
b = 20
print(a+b)
print(a-b)
print(a**b)
print(a/b)

# booleans
is_student = True
print("Is student:", is_student)

#type
print(type(age))
print(type(name))
print(type(is_student))

# type conversion
number = "25"
c_no = int(number)
print(c_no)

city = input("Enter your city: ")
print(f"I live in {city}.")

# Temperature converter
celsius = float(input())
fahrenheit = (celsius * 9 / 5) + 32
print(f"Fahrenheit: {fahrenheit:.2f}")

# String methods
word = "python programming"
print(word.upper())
print(word.title())
print(word.replace("python", "Java"))

# String formatting and length
full_name = input("Enter your full name: ").strip()
print("Formatted name:", full_name.title())
print("Number of characters:", len(full_name))


