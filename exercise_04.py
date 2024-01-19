x=int(input("Enter an integer greater than 1: "))
fl=[]
while(x<1):
    x=int(input("Please enter an integer greater than 1: "))
for num in range(x):
    f=float(input(f"Enter number #{num+1}: "))
    fl.append(f)

print(f"List of floaters: {fl}")
p=sum(fl)/x
print(f"The average is: {p}")