from inputFileFuncs import *

theText = loadText("W3/aBitOfLightReading.txt")
title = theText[0:65]

print(replaceTitular(title, "Billy"))
print(replacePunc(title))
print(splitText(title))
print(uniqueWords(title))
print(numVowels(title))
