userInput='bonk'
allNum=[]
evenNum=[]
def is_even(x):
    if(x%2==0):
        return True
    return False

while(userInput!='QUIT'):
    userInput=input("Enter a number or QUIT to quit:" )
    if(userInput=='QUIT'):
        break
    else:
        allNum.append(int(userInput))
for element in allNum:
    if(is_even(element)):
        evenNum.append(element)
print(evenNum)

