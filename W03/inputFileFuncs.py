def loadText(filepath):
    print(filepath)
    with open(filepath) as f:
        data = f.read()
        return data
    
def replaceTitular(text : str, newName):
    return text.replace("HAMLET", newName.upper())

def replacePunc(text):
    punctuation = {',', '.'}
    for char in punctuation:
        text = text.replace(char, '')
    return text

def splitText(text):
    text = text.split(' ')
    print("Size of list:", len(text))
    return text

def uniqueWords(text):
    text = text.split(' ')
    unique = set(text)
    print("Unique words:", len(unique))
    return unique

def numVowels(text):
    vowels = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    for char in text:
        if char in vowels:
            vowels[char] += 1
    return vowels

