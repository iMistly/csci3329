# Conditional statements
age = 0

while(age <= 0):
    try:
        age = int(input("How old are you?: "))
        if(age<=0):
            print("Number must be positive.")
    except:
        print("That is invalid! Please try again...")
    
if(age < 13):
    print("You are a child!")
elif(age <= 19):
    print("You are a teenager!")
else:
    print("You are old!")