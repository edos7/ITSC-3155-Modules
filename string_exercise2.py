userInput=input("Please enter a string:")
userInputArray=[]
for char in userInput:
    if(char.islower()):
        userInputArray+=char

for char in userInput:
    if(char.isupper()):
        userInputArray+=char

for x in userInputArray:
    print(x,end="")
