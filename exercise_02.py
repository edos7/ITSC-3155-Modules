x=input("Enter the first word: ")
y=input("Enter the second word: ")
if(y.endswith(x) or x.endswith(y)):
    print("True")
else:
    print("False")
