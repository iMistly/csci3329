# Single Comment
'''
Multi-line Comment
'''

# I/O
print("Hello")
print('Hello')
print("Greg's notebook")
print('Greg\'s notebook')

# Object/variables
x = 9
x += 1 # No x++ :c

# Weakly type variables
name = "Tom"
letter = 'u' 
deci = 7.2

if True:
    x += 1
    print("no curely brackets")

# Formatted strings
a = 1
b = 2

print("A is: " + str(a))
print("A is:", a)
print(f"A is: {a}")

print("The values of a, b, and x are",a,",",b,"and",x)
print("The values of a, b, and x are " + str(a) + ", " + str(b) + " and " + str(x))
print(f"The values of a, b, and x are {a}, {b} and {x}")
print(f"If we add a and b, we get {a+b}")

print(f"Here are some objects: {deci}, {name}, {letter}")

# User input
x = input("Please enter a number: ")
print(type(x))

# Typecasting
x = int(x)
print(type(x))
print(x+1)
x = str(x)
print(type(x))

# Input + Typecasting
a = int(input("Please enter another number: "))
print(type(a))

# Practice
userName = input("What is your name?: ")
userNum = int(input("What is your favorite number?: "))

print(f"Hello {userName}, {1000*userNum} is 1000x your favorite number!")

if userNum%2 == 0:
    print(f"{userNum} is even")
elif userNum > 10:
    print("That's a large number")
else:
    print(f"{userNum} is odd")
print("Last message")