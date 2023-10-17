def branch(num):
    if(num & 1):
        print("odd")
        if(num>100):
            print("weird")
    else:
        print(num*100)
        
# uInput = int(input("Enter a number: "))
        
# branch(uInput)

for i in range(40):
    print(i)
    
num = 0
while(num < 40):
    print(num)
    num += 3

myList = []
for i in range(10, -11, -1):
    myList.append(i)

print(myList)

myList = []
num = 10
while(num >= -10):
    myList.append(num)
    num -= 1
    
print(myList)

for x in myList:
    print(x)

for i in range(len(myList)):
    print(myList[i])
