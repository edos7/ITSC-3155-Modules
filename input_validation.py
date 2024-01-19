#Emir Dostovic
#Used chatGPT to find the isDigit function for input validation check
total=0
counter=0
while counter<5:
    userInput=input(f"Enter integer # {counter+1}: ");
    if(userInput.isdigit()):
        total+=int(userInput)
        counter+=1
    else:
        print("Invalid input. Please enter an int: ")
      

print("Your sum is: ",total)
    
