# # imports all functions of file
# # Requires the use of moduleName.function()
# import stringFuncs

# # Extracts a function from a module
# # Does not require the module name and can be accessed as function()
# from stringFuncs import lengthStr

# Extracts all functions from a module
from stringFuncs import *

msg = input("Enter a message: ")

print(f"The length of '{msg}' is", lengthStr(msg))
print(f"The number of vowels in '{msg}' is", numVowels(msg))
print(noSpaces(msg))