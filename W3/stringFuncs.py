def lengthStr(x):
    '''
    This function evaluates the length of the string.
    For practice purposes only.
    '''
    return len(x)

# Returns the number of vowels in a string
def numVowels(x):
    num = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    print(f"List of vowels in '{x}': ", end='')
    for letter in x:
        for char in vowels:
            if(letter.upper() == char):
                print(letter.upper(), end=' ')
                num += 1
                break
    print()
    return num
# Converts spaces in a string to underscores ("_")
def noSpaces(x):
    newString = ""
    for i in range(len(x)):
        if(x[i] == ' '):
            newString += '_'
        else:
            newString += x[i]
    return newString